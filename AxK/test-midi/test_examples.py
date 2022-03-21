# -*- coding: utf-8 -*-
# This source code is issued under MIT license. Copyright (c) 2017 Tino Wildenhain

import re
import struct
from yamaha_sysex import *

# test and explore different messages from A5000

mappings={'control_function_map':control_function_map,
          'control_device_map':control_device_map}

BP=re.compile(r"b[0-9](?:-[0-9]+)?:")

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
            for i in range(count):
                print "%s%4d Easy Edit" % (ofs,idx+i*size)
                display(data[idx+i*size:idx+i*size+size],Easy_Edit_Parameter_Block,ofs+'%d eepb ' % i)
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

a.dump_bulk_cb(sy_dump)
print "-----------------------------------------------------"
print "              system dump                            "
print "-----------------------------------------------------"
print
display(a.bulk_data,System_Parameter_Bulk_Dump, 'sy ')

a.dump_bulk_cb(pg_dump_001)
print "-----------------------------------------------------"
print "              program dump '001'                     "
print "-----------------------------------------------------"
print
display(a.bulk_data,Program_Bulk_Dump,'pd ')

a.dump_bulk_cb(sb_dump_gpiano)
print "-----------------------------------------------------"
print "              sample bank dump 'Gnd/Piano St'        "
print "-----------------------------------------------------"
print
display(a.bulk_data,Sample_Bank_Bulk_Dump,'sb ')

a.dump_bulk_cb(sp_dump_gpiano_26)
print "-----------------------------------------------------"
print "              sample dump 'Gnd/PianoS 026'"
print "-----------------------------------------------------"
print
display(a.bulk_data,Sample_Bulk_Dump,'sp ')


a.dump_bulk_cb(wd_dump_gp_left)
print "-----------------------------------------------------"
print "              wave dump 'Piano   ff*026-L'"
print "-----------------------------------------------------"
print
display(a.bulk_data,Wave_Data_Bulk_Dump,'wd ')


m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x53, 0x59, 0x53, 0x79, 0x73, 0x74, 0x65, 0x6d, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73))

ol=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x4f, 0x4c, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x20, 0x4c, 0x69, 0x73, 0x74, 0x20, 0x20, 0x20, 0x20, 0x20))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x4f, 0x4c, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x20, 0x4c, 0x69, 0x73, 0x74, 0x20, 0x20, 0x20, 0x20, 0x20))

m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x53, 0x59, 0x53, 0x79, 0x73, 0x74, 0x65, 0x6d, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x4f, 0x4c, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x20, 0x4c, 0x69, 0x73, 0x74, 0x20, 0x20, 0x20, 0x20, 0x20))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x53, 0x59, 0x53, 0x79, 0x73, 0x74, 0x65, 0x6d, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x4f, 0x4c, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x20, 0x4c, 0x69, 0x73, 0x74, 0x20, 0x20, 0x20, 0x20, 0x20))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x53, 0x59, 0x53, 0x79, 0x73, 0x74, 0x65, 0x6d, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x4f, 0x4c, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x20, 0x4c, 0x69, 0x73, 0x74, 0x20, 0x20, 0x20, 0x20, 0x20))
m=mido.Message('sysex',data=(0x43, 0x20, 0x7a, 0x4c, 0x4d, 0x20, 0x20, 0x30, 0x32, 0x37, 0x38, 0x53, 0x50, 0x73, 0x69, 0x6e, 0x65, 0x20, 0x77, 0x61, 0x76, 0x65, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x2a))
m=mido.Message('sysex',data=(0x43, 0x10, 0x58, 0x00, 0x73, 0x69, 0x6e, 0x65, 0x20, 0x77, 0x61, 0x76, 0x65, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x2a, 0x10))
m=mido.Message('sysex',data=(0x43, 0x10, 0x58, 0x01, 0x02, 0x53, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00))
m=mido.Message('sysex',data=(0x43, 0x10, 0x58, 0x00, 0x73, 0x69, 0x6e, 0x65, 0x20, 0x77, 0x61, 0x76, 0x65, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x2a, 0x10))


