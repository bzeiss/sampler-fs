#!/usr/bin/env python -i
# This source code is issued under MIT license. Copyright (c) 2017 Tino Wildenhain


import mido
import re
import struct
import time

from yamaha_sysex import *

VIS=re.compile("[a-zA-Z0-9_\-\*+\.!$\ ]")

ifacename='USB Midi:USB Midi MIDI 1 24:0'
ifacename=[i for i in mido.get_output_names() if ('USB' in i) or i.startswith('CH345') or ('MidiSport' in i)][0]


mappings={'control_function_map':control_function_map,
          'control_device_map':control_device_map}

BP=re.compile(r"b[0-9](?:-[0-9]+)?:") # 

AN=re.compile("([a-zA-Z][a-zA-Z/\ ]+[a-zA-Z0-9])") # attribute names

def bitmap(value,description):
    rv=dict()
    l=[([int(i) for i in k[1:-1].split("-")],v.strip().rstrip(",")) for k,v in zip(BP.findall(description),BP.split(description)[1:])]
    for k,v in l:
        m=0
        if len(k)==2:
            k.sort()
            for i in range(k[0],k[1]+1):
                m|=1<<i
            r=(value & m)>>k[0]
        else:
            m=1<<k[0] 
            r=bool(value & m)
        rv[v+"(%s)" % bin(m)]=r
    return rv
    

def display(data,format,ofs=''):
    #print len(data),len(format)
    vmap={}
    m8=1<<7
    m16=1<<15
    m32=1<<31
    for idx,field,description in format:

        if '*' in field:
            count=int(field.split('*')[1].replace("n","0"))
        else:
            count=1
        if field.startswith("UC"):
            if count==1:
                value=data[idx]
                if ":" in field:
                    map=mappings[field.split(":")[1]]
                    value="%d %s" % (value,map[value])
            else:
                value=''.join(chr(x) for x in data[idx:idx+count])
        elif field.startswith("UL"):
            value=struct.unpack(">I",struct.pack("BBBB",*data[idx:idx+4]))[0]
        elif field.startswith("US"):
            value=struct.unpack(">H",struct.pack("BB",*data[idx:idx+2]))[0]
        elif field.startswith("SL"):
            value=struct.unpack(">i",struct.pack("BBBB",*data[idx:idx+4]))[0]
        elif field.startswith("SS"):
            value=struct.unpack(">h",struct.pack("BB",*data[idx:idx+2]))[0]
        elif field.startswith("SC"):
            value=struct.unpack(">b",struct.pack("B",data[idx]))[0]
        elif field.endswith("byte"):
            value="...%s..." % (field.replace("byte",""))
            size=int(field.replace("byte",""))
            if ']*' in description:
                count=int(description.split("]*")[1].split()[0])
        else:
            value="unknown %s" % field
        if 'reserved' in description:
            value="reserved"
            continue
        if description.strip().startswith("b"):
            value="%s -> %r" % (value,bitmap(value,description))
            print "%s%4d: %8s %s" % (ofs,idx,value,'')
            continue
            
        if description.startswith('[Common]'):
            print "Common: %d %d" % (idx,size)
            display(data[idx:idx+size],Common_Parameter_Block,ofs+'cpb ')
            continue

        if description.startswith('[Sample Parameter]'):
            print "Sample Parameter: %d %d" % (idx,size)
            display(data[idx:idx+size],Sample_Parameter_Block,ofs+'spb ')
            continue

        if description.startswith('[Easy Edit Parameter]'):
            size=56
            count=count or int((len(data)-idx)/size)
            print '[Easy Edit Parameter]',size,count
            if '(number of assigned samples)' in description:
                count=vmap.get("number of assigned samples",count)
            value=[]
            for i in range(count):
                print "%s%4d Easy Edit" % (ofs,idx+i*size)
                value.append(display(data[idx+i*size:idx+i*size+size],Easy_Edit_Parameter_Block,ofs+'%d eepb ' % i))
                vmap["Easy_Edit_Parameter"]=value
            continue

        if description.startswith('[Effect Parameter]'):
            size=120
            count=count or int((len(data)-idx)/size)
            for i in range(count):
                print "%s%4d Easy Edit" % (ofs,idx+i*size)
                display(data[idx+i*size:idx+i*size+size],Effect_Parameter_Block,ofs+'%d efpb ' % i)
            continue
        if description.startswith('[Sample Bank Member]'):
            size=20
            count=count or int((len(data)-idx)/size)
            for i in range(count):
                print "%s%4d Sample Bank Member" % (ofs,idx+i*size)
                display(data[idx+i*size:idx+i*size+size],Sample_Bank_Member,ofs+'%d sbm ' % i)
            continue
        if description.startswith('[Control]'):
            size=4
            count=count or int((len(data)-idx)/size)
            for i in range(count):
                print "%s%4d Control Parameter Block (%d)" % (ofs,i*size+idx,size)
                display(data[idx+i*size:idx+i*size+size],Control_Parameter_Block,ofs+'%d ctpb ' % i)
            continue        
        print "%s%4d: %32r %s" % (ofs,idx,value,description)
        an=AN.search(description)
        if an:
            vmap[an.group(1)]=value
    return vmap


class AxK(object):
    def __init__(self,midiport):
        try:
            self.inport=mido.open_input(midiport,callback=self.callback)
        except Exception,x:
            print x
            pass
        try:
            self.outport=mido.open_output(midiport)
            self._send=self.outport.send
        except:
            pass

        self.callbacks=[]
        self.channel=0 # Midi-Channel 1
        self.ident()
        self.device_name="?"
        self.ident_version="?"
        self.programs={}
        self.dumps=[]
        
    def send(self,msg):
        self.buffer=[]
        self._send(msg)
        
    def __repr__(self):
        return "%s(%r) # %s (v %s)" % (self.__class__.__name__,self.outport,self.device_name,self.ident_version)
    

    def callback(self,msg):
        print "Incoming:"
        self.hexdump(msg.bytes()[:64])
        
        if msg.type!='sysex':
            if msg.type=='note_on' and msg.time==0:
                self.buffer.append(msg.note)
                self.buffer.append(msg.velocity)
                print msg.note,msg.velocity,
            else:
                print msg
            return
        self.last_msg=msg
        self.dumps.append(msg)
        
        for c in self.callbacks:
            try:
                r=c(msg)
                if r:
                    return
            except Exception,x:
                raise(x)
    def to_code(self,msg):
        print "m=mido.Message('sysex',data=(%s))" % ', '.join('0x%02x' % x for x in msg.data)

    def to_midi(self,value,size=2):
        v=value
        l=[]
        for i in range(size):
            l.append(v & 127)
            v>>=7
        if v:
            raise ValueError("Value %d too big for %d bytes" % (value,size))
        return tuple(l)

    def from_ymidi(self,data):
        return reduce(lambda a,b:(a<<7)+b,data)

    def from_midi(self,data):
        return reduce(lambda a,b:(a<<7)+b,reversed(data))

    def ident(self):
        m=mido.Message('sysex',data=(0x7e,self.channel,0x06,0x01))
        self.callbacks.append(self.ident_cb)
        self.send(m)

    def ident_cb(self,msg):
        if len(msg.data)==13 and msg.data[:5]==(126, self.channel, 6, 2, 67):
            self.device_family_number=msg.data[8]*128+msg.data[7]
            if self.device_family_number==2817:
                self.device_family_number=278 # byte order changed
            self.device_family_code=msg.data[6]*128+msg.data[5]
            self.device_name={474:"A4000",475:"A5000",278:"A3000"}.get(self.device_family_number,"?")
            self.device_ident=tuple(ord(c) for c in ("%04d" % self.device_family_number))
            self.ident_version="%02x"*4 % msg.data[14:8:-1]
            self.callbacks.remove(self.ident_cb)

    def dump_sample(self,number):
        self.sample_data=[]
        self.callbacks.append(self.dump_sample_cb)
        m=mido.Message('sysex',data=(0x7e,0,3)+self.to_midi(number,2))
        self.send(m)

    def dump_sample_cb(self,msg):
        if msg.data[:3]==(126,self.channel,1): # dump header
            self.sample_format=msg.data[5]
            self.sample_period=self.from_midi(msg.data[6:9])
            self.sample_length=self.from_midi(msg.data[9:12])
            self.sample_s_loop_start=self.from_midi(msg.data[12:15])
            self.sample_s_loop_end=self.from_midi(msg.data[15:18])
            self.sample_loop_type=msg.data[18]
            self.sample_data=[0]*3*self.sample_length

        elif msg.data[:3]==(126,self.channel,2): # data packet
            pn=msg.data[3]
            self.sample_data[pn*120:pn*120+120]=msg.data[4:]
            ack=mido.Message('sysex',data=(0x7e,self.channel,0x7f,pn))
            self.send(ack)


    def dump_bulk(self,data_type='PG',name=''):
        self.callbacks.append(self.dump_bulk_cb)
        m=mido.Message('sysex', data=(0x43,0x20+self.channel,0x7a)+tuple(ord(x) for x in ("LM  %04d%2s%-16s" % (self.device_family_number,
                                                                                                                data_type,name))))
        print "Sending:"
        self.hexdump(m.bytes())
        self.send(m)

    def dump_pg(self,name):
        "bulk dump program" 
        self.dump_bulk('PG',name)
        
    def dump_sy(self):
        "bulk dump system"
        self.dump_bulk('SY')
        
    def dump_sp(self,name):
        "bulk dump sample"
        self.dump_bulk('SP',name)
        
    def dump_sb(self,name):
        "bulk dump sample bank"
        self.dump_bulk('SB',name)
    
    def dump_ol(self):
        "bulk dump object list"
        self.dump_bulk('OL')
    
    def dump_sq(self,name):
        "bulk dump sequence"
        self.dump_bulk('SQ',name)
        
    def dump_wd(self,name):
        "bulk dump wave data"
        self.dump_bulk('WD',name)
        
    def push_fkey(self,number):
        "push function key 1...6"
        if 0<number<7:
            self.switch_remote(number-1,64)

    def push_knob(self,number):
        "push knob 1...6"
        if 0<number<7:
            self.switch_remote(number+13,64)
    
    def push_command(self):
        "push COMMAND/EXIT"
        self.switch_remote(6,64)
    
    def push_assignable(self):
        "push ASSIGNABLE"
        self.switch_remote(7,64)
        
    def push_audition(self):
        "push AUDITION"
        self.switch_remote(8,64)
    
    def push_play(self):
        "push PLAY"
        self.switch_remote(9,64)

    def push_edit(self):
        "push EDIT"
        self.switch_remote(10,64)

    def push_rec(self):
        "push REC"
        self.switch_remote(11,64)
        
    def push_disk(self):
        "push DISK"
        self.switch_remote(12,64)

    def push_utility(self):
        "push UTILITY"
        self.switch_remote(13,64)

    def push_command_assignable(self):
        "push COMMAND/EXIT+ASSIGNABLE"
        self.switch_remote(20,64)

    def push_command_audition(self):
        "push COMMAND/EXIT+AUDITION"
        self.switch_remote(21,64)
        
    def turn_knob(self,number,value=0):
        if (0 < number < 7) and (-64 < value < 64):
            self.switch_remote(122+number,value+64)
    
        
    def name16(self,name):
        return tuple(ord(c) for c in ("%-16s" % name))

    def dump_bulk_cb(self,msg):
        if msg.data[:3]==(0x43,self.channel,0x7a):
            if self.dump_bulk_cb in self.callbacks:
                self.callbacks.remove(self.dump_bulk_cb)
            self.bulk_data=msg.data
            self.bulk_size=self.from_ymidi(msg.data[3:5])
            self.bulk_name=''.join(chr(x) for x in msg.data[15:31]).rstrip()
            self.bulk_data=[(msg.data[i]<<4)+msg.data[i+1] for i in range(31,min(5+self.bulk_size,len(msg.data)-2),2)]
            #self.hexdump(self.bulk_data)
            print "dump_bulk"
            if msg.data[5:15]==(76, 77, 32, 32, )+self.device_ident+( 83, 89):
                display(self.bulk_data,System_Parameter_Bulk_Dump, 'sy ')
            elif msg.data[5:15]==(76, 77, 32, 32, )+self.device_ident+( 80, 71):
                if self.device_family_number==278:
                    d=display(self.bulk_data,Program_Bulk_Dump_a3k, 'pg3 ')
                else:
                    d=display(self.bulk_data,Program_Bulk_Dump, 'pg ')
                print d
            elif msg.data[5:15]==(76, 77, 32, 32, )+self.device_ident+( 83, 66):
                display(self.bulk_data,Sample_Bank_Bulk_Dump,'sb ')
            elif msg.data[5:15]==(76, 77, 32, 32, )+self.device_ident+( 83, 80):
                display(self.bulk_data,Sample_Bulk_Dump,'sp ')
            elif msg.data[5:15]==(76, 77, 32, 32, )+self.device_ident+( 79, 76):
                display(self.bulk_data,Object_List_Bulk_Dump,'ol ')
            return True

    def parameter_request(self,param):
        m=mido.Message('sysex',data=(0x43,0x30+self.channel,0x58,0x01)+((param)+(0,)*6)[:6])
        print "Sending parameter request (object)"
        self.hexdump(m.bytes())
        self.send(m)
        
    def system_parameter(self,parameter,data):
        param=(parameter+(0,0,0,0,0,0))[:6]
        m=mido.Message('sysex',data=(0x43,0x10+self.channel,0x58,0x02)+param+tuple(data))
        print "Sending parameter change (system parameter)"
        self.hexdump(m.bytes())
        self.send(m)
        
    def object_select(self,obj_type,obj_name):
        tid={'PG':20,'SB':17,'SP':16,'WD':2,'SQ':19}.get(obj_type)
        m=mido.Message('sysex',data=(0x43,0x10+self.channel,0x58,0x00)+tuple(ord(c) for c in ("%-16s" % obj_name))+(tid,))
        print "Sending parameter change (object select)"
        self.hexdump(m.bytes())
        self.send(m)
        self.active_object="%s:%s" % (obj_type,obj_name)

    def object_edit(self,parameter,data):
        m=mido.Message('sysex',data=(0x43,0x10+self.channel,0x58,0x01)+tuple(parameter)+tuple(data))
        print "Sendung parameter change for %s (object edit)" % self.active_object
        self.hexdump(m.bytes())
        self.send(m)
        
    def set_pg_name(self,pg_num,pg_name):
        pg_num=int(pg_num)
        if 0<pg_num<129:
            self.object_select('PG','%03d' % pg_num)
            time.sleep(0.1)
            name=("%-8s" % pg_name)[:8]
            nv=tuple(int(c,16) for c in ''.join('%02x' % ord(i) for i in name))
            self.object_edit((1,0,0,0,0,0),nv)
        
        
    def switch_remote(self,switch_number,data):
        m=mido.Message('sysex',data=(0x43,0x10+self.channel,0x58,0x03,switch_number,0,0,0,0,0,data))
        self.send(m)
        
    def object_link(self,from_obj,to_obj,link=False):
        """from_obj, to_obj TYPE:Name TYPE=two letter: PG, SB, SP, WD"""
        fot,fob=from_obj.split(":",1)
        tot,tob=to_obj.split(":",1)
        fid={'PG':20,'SB':17,'SP':16,'WD':2,'SQ':19}.get(fot)
        tid={'PG':20,'SB':17,'SP':16,'WD':2,'SQ':19}.get(tot)
        m=mido.Message('sysex',data=(0x43,0x10,0x58,0x04,)+self.name16(fob)+(fid,)+self.name16(tob)+(tid,int(link)))
        self.send(m)

    def print_sample_data(self):
        for i in range(self.sample_length):
            print (reduce(lambda a,b:(a<<7)+b,tuple(self.sample_data[i*3:i*3+3]))>>5)-32768
    def hexdump(self,data):
        for i in range(0,len(data),16):
             print "%05d: %-48s %-16s" % (i," ".join("%02x" % j for j in data[i:i+16]),''.join(chr(j) if VIS.match(chr(j)) else '.' for j in data[i:i+16]))

    def text2char(self,text,lenght=None):
            if lenght:
                text=(("%%-%ds" % length) % text)[:length]
            return tuple(ord(c) for c in text)




a=AxK(ifacename)
