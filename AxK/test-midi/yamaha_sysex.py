# -*- coding: utf-8 -*-
# This source code is issued under MIT license. Copyright (c) 2017 Tino Wildenhain

# not yet fully developed wrapper classes
class UC(object):
	def __init__(self,offset,name,length=1):
		self.offset=offset
		self.name=name
		self.lenght=length
	

class YMapper(object):
	def __init__(self,format):
		self.format=format
		

# data structures generated and optimized from documentation

# 1.1.1 Program Bulk Dump 408+56*(number of samples)byte
# offset data size value name
Program_Bulk_Dump=(
	(0, "64byte",'''[Common]'''), #[Common]
	(64, "UC*8",'''c program name'''), #c program name
	(72, "UC",'''b b0:AD in on, b2-1:AD in source,b5-3:effect1-3 connection, b7-6:program LFO sync'''), #b b0:AD in on, b2-1:AD in source,b5-3:effect1-3 connection, b7-6:program LFO sync
	(73, "UC",'''b b2-0:program LFO cycle, b5-3:program LFO wave,b7-6:program LFO initial phase'''), #b b2-0:program LFO cycle, b5-3:program LFO wave,b7-6:program LFO initial phase
	(74, "US",'''b b0:MIDI channelA01 controller reset...b15:MIDI channelA16 controller reset'''), #b b0:MIDI channelA01 controller reset...b15:MIDI channelA16 controller reset
	(76, "US",'''b b0:MIDI channelA01 note on normal/toggle...b15:MIDI channelA16 note on normal/toggle'''), #b b0:MIDI channelA01 note on normal/toggle...b15:MIDI channelA16 note on normal/toggle
	(78, "SC",'''a63 AD in (L) pan'''), #a63 AD in (L) pan
	(79, "UC",'''-- reserved'''), #-- reserved
	(80, "UC",'''-- reserved'''), #-- reserved
	(81, "UC",'''-- reserved'''), #-- reserved
	(82, "UC",'''-- reserved'''), #-- reserved
	(83, "UC",'''0-127 program level'''), #0-127 program level
	(84, "SC",'''-- reserved'''), #-- reserved
	(85, "SC",'''-- reserved'''), #-- reserved
	(86, "SC",'''±127 program transpose'''), #±127 program transpose
	(87, "SC",'''-2,-1,0-32 program LFO reset MIDI channel (*2)'''), #-2,-1,0-32 program LFO reset MIDI channel (*2)
	(88, "UC",'''0-3 program portamento type'''), #0-3 program portamento type
	(89, "UC",'''0-127 program portamento rate'''), #0-127 program portamento rate
	(90, "UC",'''0-127 program portamento time'''), #0-127 program portamento time
	(91, "UC",'''0-127 S/H speed'''), #0-127 S/H speed
	(92, "UC",'''25-250 program LFO tempo'''), #25-250 program LFO tempo
	(93, "SC",'''-1,0-127 program LFO reset note (*2)'''), #-1,0-127 program LFO reset note (*2)
	(94, "US",'''0-999 number of assigned samples (*1)'''), #0-999 number of assigned samples (*1)
	(96, "120byte",'''[Effect Parameter]*3 (effect1-3)'''), #[Effect Parameter]*3 (effect1-3)
	(216, "16byte",'''-- reserved'''), #-- reserved
	(232, "120byte",'''[Effect Parameter]*3 (effect4-6) (A5000 only)'''), #[Effect Parameter]*3 (effect4-6) (A5000 only)
	(352, "16byte",'''[Control]*4 (program control1-4)'''), #[Control]*4 (program control1-4)
	(368, "US",'''b b0:MIDI channel B01 controller reset...b15:MIDI channel B16 controller reset (A5000 only)'''), #b b0:MIDI channel B01 controller reset...b15:MIDI channel B16 controller reset (A5000 only)
	(370, "US",'''b b0:MIDI channel B01 note on normal/toggle...b15:MIDI channel B16 note on normal/toggle(A5000 only)'''), #b b0:MIDI channel B01 note on normal/toggle...b15:MIDI channel B16 note on normal/toggle(A5000 only)
	(372, "UC",'''b b2-0:effect4-6 connection (A5000 only)'''), #b b2-0:effect4-6 connection (A5000 only)
	(373, "UC",'''0-12 AD in (L) output1 (*4)'''), #0-12 AD in (L) output1 (*4)
	(374, "UC",'''0-127 AD in (L) level1'''), #0-127 AD in (L) level1
	(375, "UC",'''0-12 AD in (L) output2 (*4)'''), #0-12 AD in (L) output2 (*4)
	(376, "UC",'''0-127 AD in (L) level2'''), #0-127 AD in (L) level2
	(377, "SC",'''±63 AD in R pan'''), #±63 AD in R pan
	(378, "UC",'''0-12 AD in R output1 (*4)'''), #0-12 AD in R output1 (*4)
	(379, "UC",'''0-127 AD in R level1'''), #0-127 AD in R level1
	(380, "UC",'''0-12 AD in R output2 (*4)'''), #0-12 AD in R output2 (*4)
	(381, "UC",'''0-127 AD in R level2'''), #0-127 AD in R level2
	(382, "UC*16",'''0-127 program LFO step wave value1-16'''), #0-127 program LFO step wave value1-16
	(398, "UC",'''b b2-0:total steps of step wave, b4-3:step wave slope'''), #b b2-0:total steps of step wave, b4-3:step wave slope
	(399, "9byte",'''-- reserved'''), #-- reserved
	(408, "56*n",'''[Easy Edit Parameter]*(number of assigned samples)'''), #byte [Easy Edit Parameter]*(number of samples)
)

# 1.1.1 Program Bulk Dump 232+56*(number of samples)byte
# offset data size value name
Program_Bulk_Dump_a3k=(
	(0, "64byte",'''[Common]'''), #[Common]
	(64, "UC*8",'''c program name'''), #c program name
	(72, "UC",'''b b0:AD in on, b2-1:AD in source,b5-3:effect1-3 connection, b7-6:program LFO sync'''), #b b0:AD in on, b2-1:AD in source,b5-3:effect1-3 connection, b7-6:program LFO sync
	(73, "UC",'''b b2-0:program LFO cycle, b5-3:program LFO wave,b7-6:program LFO initial phase'''), #b b2-0:program LFO cycle, b5-3:program LFO wave,b7-6:program LFO initial phase
	(74, "US",'''b b0:MIDI channelA01 controller reset...b15:MIDI channelA16 controller reset'''), #b b0:MIDI channelA01 controller reset...b15:MIDI channelA16 controller reset
	(76, "US",'''b b0:MIDI channelA01 note on normal/toggle...b15:MIDI channelA16 note on normal/toggle'''), #b b0:MIDI channelA01 note on normal/toggle...b15:MIDI channelA16 note on normal/toggle
	(78, "SC",'''a63 AD in (L) pan'''), #a63 AD in (L) pan
	(79, "UC",'''-- reserved'''), #-- reserved
	(80, "UC",'''-- reserved'''), #-- reserved
	(81, "UC",'''-- reserved'''), #-- reserved
	(82, "UC",'''-- reserved'''), #-- reserved
	(83, "UC",'''0-127 program level'''), #0-127 program level
	(84, "SC",'''±63 fine tune'''), #-- reserved
	(85, "SC",'''±127 coarse tune'''), #-- reserved
	(86, "SC",'''±127 program transpose'''), #±127 program transpose
	(87, "UC",'''-- reserved'''), #-2,-1,0-32 program LFO reset MIDI channel (*2)
	(88, "UC",'''0-3 program portamento type'''), #0-3 program portamento type
	(89, "UC",'''0-127 program portamento rate'''), #0-127 program portamento rate
	(90, "UC",'''0-127 program portamento time'''), #0-127 program portamento time
	(91, "UC",'''0-127 S/H speed'''), #0-127 S/H speed
	(92, "US",'''-- reserved'''), #25-250 program LFO tempo
	(94, "US",'''0-999 number of assigned samples (*1)'''), #0-999 number of assigned samples (*1)
	(96, "120byte",'''[Effect Parameter]*3 (effect1-3)'''), #[Effect Parameter]*3 (effect1-3)
	(216, "16byte",'''[Control]*4 (program control1-4)'''), #[Control]*4 (program control1-4)
	(232, "56*n",'''[Easy Edit Parameter]*(number of assigned samples)'''), #byte [Easy Edit Parameter]*(number of samples)
)


# 1.1.2 Sample Bank Bulk Dump 312+20*(number of samples)byte
# offset data size value name
Sample_Bank_Bulk_Dump=(
	(0, "64byte",'''[Common]'''), #[Common]
	(64, "224byte",'''[Sample Parameter]'''), #[Sample Parameter]
	(288, "UL",'''b sample bank value enable (*1)'''), #b sample bank value enable (*1)
	(292, "UL",'''b sample bank value enable (*2)'''), #b sample bank value enable (*2)
	(296, "UL",'''b sample bank value enable (*3)'''), #b sample bank value enable (*3)
	(300, "UL",'''-- reserved'''), #-- reserved
	(304, "UC",'''0-127 number of assigned samples'''), #0-127 number of assigned samples
	(305, "UC*7",'''-- reserved'''), #-- reserved
	(312, "20*n",'''[Sample Bank Member]*(number of samples)'''), #byte [Sample Bank Member]*(number of samples)
)


# 1.1.3 Sample Bulk Dump 336byte
# offset data size value name
Sample_Bulk_Dump=(
	(0, '64byte', '[Common]'),
	(64, 'UC*16', 'c linked wave object name L (*1)'),
	(80, 'UC*16', 'c linked wave object name R (*1)'),
	(96, 'UL*2', '— reserved'),
	(104, 'UL*2', '— reserved'),
	(112, '224byte', '[Sample Parameter]'),
)
#(*1) No assignment when the ﬁrst byte is $00.

#1.1.4 Wave Data Bulk Dump 72+2*(wave data word size)byte
#offset data size value name
Wave_Data_Bulk_Dump=(
	(0, "64byte",'''[Common]'''), #[Common]
	(64, "SS",'''-- reserved'''), #-- reserved
	(66, "US",'''-- reserved'''), #-- reserved
	(68, "US",'''-- reserved'''), #-- reserved
	(70, "US",'''-- reserved'''), #-- reserved
	(72, "US*n",'''wave data (n='size' in [Common])'''), #wave data (n='size' in [Common])
)
# 1.1.5 Sequence Bulk Dump 72+(sequence data byte size)byte
# offset data size value name
Sequence_Bulk_Dump=(
	(0, "64byte",'''[Common]'''), #[Common]
	(64, "US",'''50-250 original tempo'''), #50-250 original tempo
	(66, "US",'''-- reserved'''), #-- reserved
	(68, "US",'''-- reserved'''), #-- reserved
	(70, "US",'''-- reserved'''), #-- reserved
	(72, "UC*n",'''sequence data (n='size' in [Common])'''), #sequence data (n='size' in [Common])
)

# Object List Bulk Dump 17*(number of all objects)byte
# offset data size value name
Object_List_Bulk_Dump=(
	(0, "UC",'''object type (sample:16, sample bank:17, sequence:19, program:20)'''), #object type (sample:16, sample bank:17, sequence:19, program:20)
	(1, "UC*16",'''c name'''), #c name
)
# 1.1.7 Parameter Block
# [Common]  64byte
# offset data size value name
Common_Parameter_Block=(
	(0, "UC",'''object type (sample:16, sample bank:17, sequence:19, program:20)'''), #object type (sample:16, sample bank:17, sequence:19, program:20)
	(1, "UC",'''-- reserved'''), #-- reserved
	(2, "UC*16",'''c name'''), #c name
	(18, "UC*2",'''-- reserved'''), #-- reserved
	(20, "UL",'''size (wave data word size for wave data bulk dump, sequence data word size for sequence bulk dump, 0 in all other cases.)'''), #size (wave data word size for wave data bulk dump, sequence data word size for sequence bulk dump, 0 in all other cases.)
	(24, "UC*16",'''-- reserved'''), #-- reserved
	(40, "UC*16",'''-- reserved'''), #-- reserved
	(56, "UC",'''-- reserved'''), #-- reserved
	(57, "UC*3",'''-- reserved'''), #-- reserved
	(60, "UL",'''-- reserved'''), #-- reserved
)

#[Control]  4byte 
#offset data size value name
Control_Parameter_Block=(
	(0, "UC:control_device_map",'''0-126 control device'''), #0-126 control device
	(1, "UC:control_function_map",'''0-m control function (program:m=71(A4000),128(A5000), sample:m=36)'''), #0-m control function (program:m=71(A4000),128(A5000), sample:m=36)
	(2, "UC",'''0-3 control type'''), #0-3 control type
	(3, "SC",'''±63 control range'''), #±63 control range
)

#[Sample Parameter]  224byte
#offset data size value name

Sample_Parameter_Block=(
	(0, "24byte",'''-- reserved'''), #-- reserved
	(24, "UL",'''b b0:linked to program001 -- b31:program032'''), #b b0:linked to program001 -- b31:program032
	(28, "UL",'''b b0:linked to program033 -- b31:program064'''), #b b0:linked to program033 -- b31:program064
	(32, "UL",'''b b0:linked to program065 -- b31:program096'''), #b b0:linked to program065 -- b31:program096
	(36, "UL",'''b b0:linked to program097 -- b31:program128'''), #b b0:linked to program097 -- b31:program128
	(40, "UC",'''b b0:sample bank member (*8), b1:mono sample,b2:expanded (1 for mono samples when detune or dephase is not +/-0)'''), #b b0:sample bank member (*8), b1:mono sample,b2:expanded (1 for mono samples when detune or dephase is not +/-0)
	(41, "UC",'''b b0:reserved, b1:mono mode,b2:key x-fade on, b3:reserved,b4:fixed pitch on, b7-6:EQ type'''), #b b0:reserved, b1:mono mode,b2:key x-fade on, b3:reserved,b4:fixed pitch on, b7-6:EQ type
	(42, "UC",'''0-32 MIDI receive channel (*5)'''), #0-32 MIDI receive channel (*5)
	(43, "UC",'''0-13 pitch bend type'''), #0-13 pitch bend type
	(44, "UC",'''0-24 pitch bend range'''), #0-24 pitch bend range
	(45, "SC",'''±127 coarse tune'''), #±127 coarse tune
	(46, "UC",'''0-127 original key L'''), #0-127 original key L
	(47, "UC",'''0-127 original key R (*7)'''), #0-127 original key R (*7)
	(48, "US",'''1-65535 sampling frequency L'''), #1-65535 sampling frequency L
	(50, "US",'''1-65535 sampling frequency R (*7)'''), #1-65535 sampling frequency R (*7)
	(52, "SC",'''±63 fine tune L'''), #±63 fine tune L
	(53, "SC",'''±63 fine tune R (*7)'''), #±63 fine tune R (*7)
	(54, "SS*2",'''-- reserved'''), #-- reserved
	(58, "UC",'''0-127,128 key range high ( >=low)  (*2)'''), #0-127,128 key range high ( >=low)  (*2)
	(59, "SC",'''-1,0-127 key range low ( <=high) (*3)'''), #-1,0-127 key range low ( <=high) (*3)
	(60, "UC",'''-- reserved'''), #-- reserved
	(61, "UC",'''0-5 loop mode'''), #0-5 loop mode
	(62, "US",'''8000-15999 loop tempo 80.00-159.99'''), #8000-15999 loop tempo 80.00-159.99
	(64, "UL",'''0-16777215 wave start address L'''), #0-16777215 wave start address L
	(68, "UL",'''0-16777215 wave start address R (*7)'''), #0-16777215 wave start address R (*7)
	(72, "UL",'''0-16777215 wave length L'''), #0-16777215 wave length L
	(76, "UL",'''0-16777215 wave length R (*7)'''), #0-16777215 wave length R (*7)
	(80, "UL",'''0-16777215 loop start address L'''), #0-16777215 loop start address L
	(84, "UL",'''0-16777215 loop start address R (*7)'''), #0-16777215 loop start address R (*7)
	(88, "UL",'''0-16777215 loop length L (end - start +1)'''), #0-16777215 loop length L (end - start +1)
	(92, "UL",'''0-16777215 loop length R (end - start +1) (*7)'''), #0-16777215 loop length R (end - start +1) (*7)
	(96, "SC",'''±63 start address velocity sensitivity'''), #±63 start address velocity sensitivity
	(97, "UC",'''0-16 filter type (*9)'''), #0-16 filter type (*9)
	(98, "UC",'''0-127 filter cutoff frequency'''), #0-127 filter cutoff frequency
	(99, "UC",'''0-127 filter Q/width'''), #0-127 filter Q/width
	(100, "UC",'''0-127 cutoff key scaling break point 1 ( <=2)'''), #0-127 cutoff key scaling break point 1 ( <=2)
	(101, "UC",'''0-127 cutoff key scaling break point 2 ( >=1)'''), #0-127 cutoff key scaling break point 2 ( >=1)
	(102, "SC",'''±127 cutoff key scaling level 1'''), #±127 cutoff key scaling level 1
	(103, "SC",'''±127 cutoff key scaling level 2'''), #±127 cutoff key scaling level 2
	(104, "SC",'''±63,64-68 cutoff velocity sensitivity (*4)'''), #±63,64-68 cutoff velocity sensitivity (*4)
	(105, "SC",'''±63,64-68 Q/width velocity sensitivity (*4)'''), #±63,64-68 Q/width velocity sensitivity (*4)
	(106, "SC",'''±7 detune'''), #±7 detune
	(107, "SC",'''±63 dephase'''), #±63 dephase
	(108, "SC",'''±63 expand width'''), #±63 expand width
	(109, "UC",'''0-63 random pitch'''), #0-63 random pitch
	(110, "UC",'''0-127 sample level'''), #0-127 sample level
	(111, "SC",'''-64, ±63 pan (*10)'''), #-64, ±63 pan (*10)
	(112, "UC",'''0-127 velocity low limit'''), #0-127 velocity low limit
	(113, "UC",'''±127 velocity offset'''), #±127 velocity offset
	(114, "UC",'''0-127 velocity range high ( >=low)'''), #0-127 velocity range high ( >=low)
	(115, "UC",'''0-127 velocity range low ( <=high)'''), #0-127 velocity range low ( <=high)
	(116, "UC",'''0-127 level key scaling break point 1 ( <=2)'''), #0-127 level key scaling break point 1 ( <=2)
	(117, "UC",'''0-127 level key scaling break point 2 ( >=1)'''), #0-127 level key scaling break point 2 ( >=1)
	(118, "UC",'''0-127 level key scaling level 1'''), #0-127 level key scaling level 1
	(119, "UC",'''0-127 level key scaling level 2'''), #0-127 level key scaling level 2
	(120, "SC",'''±127 velocity sensitivity'''), #±127 velocity sensitivity
	(121, "UC",'''0-16 alternate group number'''), #0-16 alternate group number
	(122, "UC",'''4-58 EQ frequency'''), #4-58 EQ frequency
	(123, "SC",'''52-76 EQ gain'''), #52-76 EQ gain
	(124, "UC",'''10-120 EQ width'''), #10-120 EQ width
	(125, "SC",'''±63 cutoff distance'''), #±63 cutoff distance
	(126, "UC",'''0-127 FEG attack rate'''), #0-127 FEG attack rate
	(127, "UC",'''0-127 FEG decay rate'''), #0-127 FEG decay rate
	(128, "UC",'''0-127 FEG release rate'''), #0-127 FEG release rate
	(129, "SC",'''±127 FEG init level'''), #±127 FEG init level
	(130, "SC",'''±127 FEG attack level'''), #±127 FEG attack level
	(131, "SC",'''±127 FEG sustain level'''), #±127 FEG sustain level
	(132, "SC",'''±127 FEG release level'''), #±127 FEG release level
	(133, "SC",'''±7 FEG rate key scaling'''), #±7 FEG rate key scaling
	(134, "SC",'''±63 FEG rate velocity sensitivity'''), #±63 FEG rate velocity sensitivity
	(135, "SC",'''±63 FEG attack level velocity sensitivity'''), #±63 FEG attack level velocity sensitivity
	(136, "SC",'''±63 FEG level velocity sensitivity'''), #±63 FEG level velocity sensitivity
	(137, "UC",'''0-127 PEG attack rate'''), #0-127 PEG attack rate
	(138, "UC",'''0-127 PEG decay rate'''), #0-127 PEG decay rate
	(139, "UC",'''0-127 PEG release rate'''), #0-127 PEG release rate
	(140, "SC",'''±127 PEG init level'''), #±127 PEG init level
	(141, "SC",'''±127 PEG attack level'''), #±127 PEG attack level
	(142, "SC",'''±127 PEG sustain level'''), #±127 PEG sustain level
	(143, "SC",'''±127 PEG release level'''), #±127 PEG release level
	(144, "SC",'''±7 PEG rate key scaling'''), #±7 PEG rate key scaling
	(145, "SC",'''±63 PEG rate velocity sensitivity'''), #±63 PEG rate velocity sensitivity
	(146, "SC",'''±63 PEG level velocity sensitivity'''), #±63 PEG level velocity sensitivity
	(147, "UC",'''±63 PEG range'''), #±63 PEG range
	(148, "UC",'''0-127 AEG attack rate'''), #0-127 AEG attack rate
	(149, "UC",'''0-127 AEG decay rate'''), #0-127 AEG decay rate
	(150, "UC",'''0-127 AEG release rate'''), #0-127 AEG release rate
	(151, "UC*2",'''-- reserved'''), #-- reserved
	(153, "UC",'''0-127 AEG sustain level'''), #0-127 AEG sustain level
	(154, "UC",'''-- reserved'''), #-- reserved
	(155, "UC",'''0-2 AEG attack mode'''), #0-2 AEG attack mode
	(156, "SC",'''±7 AEG rate key scaling'''), #±7 AEG rate key scaling
	(157, "SC",'''±63 AEG rate velocity sensitivity'''), #±63 AEG rate velocity sensitivity
	(158, "UC",'''0-3 LFO wave'''), #0-3 LFO wave
	(159, "UC",'''0-127 LFO speed'''), #0-127 LFO speed
	(160, "UC",'''0-127 LFO delay time'''), #0-127 LFO delay time
	(161, "UC",'''b b0:LFO sync on, b1:cutoff mod phase invert on, b2:pitch mod phase invert on'''), #b b0:LFO sync on, b1:cutoff mod phase invert on, b2:pitch mod phase invert on
	(162, "UC",'''0-127 cutoff mod depth'''), #0-127 cutoff mod depth
	(163, "UC",'''0-127 pitch mod depth'''), #0-127 pitch mod depth
	(164, "UC",'''0-127 amplitude mod depth'''), #0-127 amplitude mod depth
	(165, "UC*4",'''-- reserved'''), #-- reserved
	(169, "SC",'''±31 filter gain'''), #±31 filter gain
	(170, "US*5",'''-- reserved'''), #-- reserved
	(180, "UL",'''0-16777215 wave end address'''), #0-16777215 wave end address
	(184, "UL",'''0-16777215 loop end address'''), #0-16777215 loop end address
	(188, "24byte",'''[Control]*6 (sample control1-6)'''), #[Control]*6 (sample control1-6)
	(212, "UC",'''0-127 velocity x-fade high'''), #0-127 velocity x-fade high
	(213, "UC",'''0-127 velocity x-fade low'''), #0-127 velocity x-fade low
	(214, "UC",'''0-12 output1'''), #0-12 output1
	(215, "UC",'''0-127 output1 level'''), #0-127 output1 level
	(216, "UC",'''0-12 output2'''), #0-12 output2
	(217, "UC",'''0-127 output2 level'''), #0-127 output2 level
	(218, "UC",'''0-5 sample portamento type'''), #0-5 sample portamento type
	(219, "UC",'''0-127 sample portamento rate'''), #0-127 sample portamento rate
	(220, "UC",'''0-127 sample portamento time'''), #0-127 sample portamento time
	(221, "UC*3",'''-- reserved'''), #-- reserved
)

#[Sample Bank Member]  20byte
#offset data size value name
Sample_Bank_Member=(
	(0, "UC*16",'''c assigned sample name'''), #c assigned sample name
	(16, "UL",'''-- reserved'''), #-- reserved
)
#[Easy Edit Parameter]  56byte
#offset data size value name
Easy_Edit_Parameter_Block=(
	(0, "UC*16",'''c assigned sample(bank) name'''), #c assigned sample(bank) name
	(16, "UL",'''-- reserved'''), #-- reserved
	(20, "UC",'''assigned object type (sample:16, sample bank:17)'''), #assigned object type (sample:16, sample bank:17)
	(21, "SC",'''-1,0-32 MIDI receive channel assign ( -1:"=sample", 0-15:A01-A16, 16:basic receive channel, 17-32:B01-16(A5000 only))'''), #-1,0-32 MIDI receive channel assign ( -1:"=sample", 0-15:A01-A16, 16:basic receive channel, 17-32:B01-16(A5000 only))
	(22, "SC",'''±127 level offset'''), #±127 level offset
	(23, "SC",'''±127 velocity sensitivity'''), #±127 velocity sensitivity
	(24, "SC",'''±127 pan offset'''), #±127 pan offset
	(25, "SC",'''±127 velocity x-fade high offset'''), #±127 velocity x-fade high offset
	(26, "SC",'''±127 fine tune offset'''), #±127 fine tune offset
	(27, "SC",'''±127 velocity x-fade low offset'''), #±127 velocity x-fade low offset
	(28, "SC",'''±127 coarse tune offset'''), #±127 coarse tune offset
	(29, "SC",'''-1,0-12 output1 (*5)'''), #-1,0-12 output1 (*5)
	(30, "UC",'''0-127 key limit high ( >=low)'''), #0-127 key limit high ( >=low)
	(31, "UC",'''0-127 key limit low ( <=high)'''), #0-127 key limit low ( <=high)
	(32, "SC",'''±127 key range shift'''), #±127 key range shift
	(33, "UC",'''0-127 velocity limit high ( >=low)'''), #0-127 velocity limit high ( >=low)
	(34, "UC",'''0-127 velocity limit low ( <=high)'''), #0-127 velocity limit low ( <=high)
	(35, "UC",'''b b0:portamento, b2:mono mode, b4:key x-fade on,b6:reserved (*3)'''), #b b0:portamento, b2:mono mode, b4:key x-fade on,b6:reserved (*3)
	(36, "SC",'''-1,0-16 alternate group number (*2)'''), #-1,0-16 alternate group number (*2)
	(37, "SC",'''±127 AEG attack rate offset'''), #±127 AEG attack rate offset
	(38, "SC",'''±127 AEG decay rate offset'''), #±127 AEG decay rate offset
	(39, "SC",'''±127 AEG release rate offset'''), #±127 AEG release rate offset
	(40, "SC",'''-1,0-12 output2 (*5)'''), #-1,0-12 output2 (*5)
	(41, "SC",'''±127 filter cutoff offset'''), #±127 filter cutoff offset
	(42, "SC",'''±63 filter gain offset'''), #±63 filter gain offset
	(43, "SC",'''±31 filter Q/width offset'''), #±31 filter Q/width offset
	(44, "SC",'''±127 cutoff distance offset'''), #±127 cutoff distance offset
	(45, "SC",'''-- reserved'''), #-- reserved
	(46, "SC",'''-- reserved'''), #-- reserved
	(47, "SC",'''±127 output1 level offset'''), #±127 output1 level offset
	(48, "SC",'''-- reserved'''), #-- reserved
	(49, "SC",'''-- reserved'''), #-- reserved
	(50, "SC",'''±127 output2 level offset'''), #±127 output2 level offset
	(51, "UC",'''0-1 MIDI control on'''), #0-1 MIDI control on
	(52, "UC",'''-- reserved'''), #-- reserved
	(53, "UC*3",'''-- reserved'''), #-- reserved
)

#[Effect Parameter]  40byte
# offset data size value name
Effect_Parameter_Block=(
	(0, "UC",'''0-1 bypass'''), #0-1 bypass
	(1, "UC",'''0-127 input level'''), #0-127 input level
	(2, "UC",'''0-127 output level'''), #0-127 output level
	(3, "SC",'''±63 output pan'''), #±63 output pan
	(4, "UC",'''0-5 output'''), #0-5 output
	(5, "SC",'''-126-0 width'''), #-126-0 width
	(6, "UC",'''0-96 effect type'''), #0-96 effect type
	(7, "UC",'''-- reserved'''), #-- reserved
	(8, "US*16",'''effect parameter1-16'''), #effect parameter1-16
)
#1.2.1 System Parameter Bulk Dump 4064byte
#offset data size value name
System_Parameter_Bulk_Dump=(
	(0, "UC*16",'''-- reserved'''), #-- reserved
	(16, "SC",'''±63 master fine tune'''), #±63 master fine tune
	(17, "SC",'''±127 master coarse tune'''), #±127 master coarse tune
	(18, "SC",'''±127 master transpose'''), #±127 master transpose
	(19, "UC",'''0-17 velocity curve'''), #0-17 velocity curve
	(20, "UC",'''0-31 MIDI basic receive channel'''), #0-31 MIDI basic receive channel
	(21, "UC",'''0-5 stereo to assignable out'''), #0-5 stereo to assignable out
	(22, "UC",'''b b0:omni on, b1:program change enable,b2:wave address auto length lock, b3:auto zero,b4:auto snap, b5:audition with easy edit,b6:audition with effect, b7:play&load'''), #b b0:omni on, b1:program change enable,b2:wave address auto length lock, b3:auto zero,b4:auto snap, b5:audition with easy edit,b6:audition with effect, b7:play&load
	(23, "UC",'''-1,0-32 knob2 control MIDI transmit channel (*3)'''), #-1,0-32 knob2 control MIDI transmit channel (*3)
	(24, "UC",'''-1,0-32 knob3 control MIDI transmit channel (*3)'''), #-1,0-32 knob3 control MIDI transmit channel (*3)
	(25, "UC",'''-1,0-32 knob4 control MIDI transmit channel (*3)'''), #-1,0-32 knob4 control MIDI transmit channel (*3)
	(26, "UC",'''-1,0-32 knob5 control MIDI transmit channel (*3)'''), #-1,0-32 knob5 control MIDI transmit channel (*3)
	(27, "UC",'''0-120 knob2 control device'''), #0-120 knob2 control device
	(28, "UC",'''0-120 knob3 control device'''), #0-120 knob3 control device
	(29, "UC",'''0-120 knob4 control device'''), #0-120 knob4 control device
	(30, "UC",'''0-120 knob5 control device'''), #0-120 knob5 control device
	(30, "UC",'''0-32 fkey1 play MIDI transmit channel'''), #0-32 fkey1 play MIDI transmit channel
	(32, "UC",'''0-32 fkey2 play MIDI transmit channel'''), #0-32 fkey2 play MIDI transmit channel
	(33, "UC",'''0-32 fkey3 play MIDI transmit channel'''), #0-32 fkey3 play MIDI transmit channel
	(34, "UC",'''0-32 fkey4 play MIDI transmit channel'''), #0-32 fkey4 play MIDI transmit channel
	(35, "UC",'''0-32 fkey5 play MIDI transmit channel'''), #0-32 fkey5 play MIDI transmit channel
	(36, "UC",'''0-32 fkey6 play MIDI transmit channel'''), #0-32 fkey6 play MIDI transmit channel
	(37, "UC",'''0-127 fkey1 play note number'''), #0-127 fkey1 play note number
	(38, "UC",'''0-127 fkey2 play note number'''), #0-127 fkey2 play note number
	(39, "UC",'''0-127 fkey3 play note number'''), #0-127 fkey3 play note number
	(40, "UC",'''0-127 fkey4 play note number'''), #0-127 fkey4 play note number
	(41, "UC",'''0-127 fkey5 play note number'''), #0-127 fkey5 play note number
	(42, "UC",'''0-127 fkey6 play note number'''), #0-127 fkey6 play note number
	(43, "UC",'''1-127 fkey1 play velocity'''), #1-127 fkey1 play velocity
	(44, "UC",'''1-127 fkey2 play velocity'''), #1-127 fkey2 play velocity
	(45, "UC",'''1-127 fkey3 play velocity'''), #1-127 fkey3 play velocity
	(46, "UC",'''1-127 fkey4 play velocity'''), #1-127 fkey4 play velocity
	(47, "UC",'''1-127 fkey5 play velocity'''), #1-127 fkey5 play velocity
	(48, "UC",'''1-127 fkey6 play velocity'''), #1-127 fkey6 play velocity
	(49, "UC",'''0-4 stereo output level offset'''), #0-4 stereo output level offset
	(50, "UC",'''4-40 total EQ low boost frequency'''), #4-40 total EQ low boost frequency
	(51, "UC",'''52-76 total EQ low boost gain'''), #52-76 total EQ low boost gain
	(52, "UC",'''b b3-0:loop remix variation, b7-4:loop remix type'''), #b b3-0:loop remix variation, b7-4:loop remix type
	(53, "UC",'''4-40 total EQ low frequency'''), #4-40 total EQ low frequency
	(54, "UC",'''52-76 total EQ low gain'''), #52-76 total EQ low gain
	(55, "UC",'''10-120 total EQ low width'''), #10-120 total EQ low width
	(56, "UC",'''4-58 total EQ mid frequency'''), #4-58 total EQ mid frequency
	(57, "UC",'''52-76 total EQ mid gain'''), #52-76 total EQ mid gain
	(58, "UC",'''10-120 total EQ mid width'''), #10-120 total EQ mid width
	(59, "UC",'''28-58 total EQ high frequency'''), #28-58 total EQ high frequency
	(60, "UC",'''52-76 total EQ high gain'''), #52-76 total EQ high gain
	(61, "UC",'''10-120 total EQ high width'''), #10-120 total EQ high width
	(62, "UC",'''0-1 program mode'''), #0-1 program mode
	(63, "UC",'''b b0:loop remix auto audition, b1:knob control MIDI out,b2:fkey play MIDI out'''), #b b0:loop remix auto audition, b1:knob control MIDI out,b2:fkey play MIDI out
	(64, "UC*32",'''0-127 multi part A01-B16 program number1-128'''), #0-127 multi part A01-B16 program number1-128
	(96, "360byte",'''loop remix registered data'''), #loop remix registered data
	(456, "UC",'''0-7 loop remix zone start point'''), #0-7 loop remix zone start point
	(457, "UC",'''1-8 loop remix zone end point ( >start)'''), #1-8 loop remix zone end point ( >start)
	(458, "UC",'''0-4 assignable L&R output level offset'''), #0-4 assignable L&R output level offset
	(459, "UC",'''0-4 assignable 1&2 output level offset'''), #0-4 assignable 1&2 output level offset
	(460, "UC",'''0-4 assignable 3&4 output level offset'''), #0-4 assignable 3&4 output level offset
	(461, "UC",'''0-4 assignable 5&6 output level offset'''), #0-4 assignable 5&6 output level offset
	(462, "UC",'''0-4 DIG&OPT output level offset'''), #0-4 DIG&OPT output level offset
	(463, "UC",'''-- reserved'''), #-- reserved
	(464, "UC",'''0-7 self SCSI ID'''), #0-7 self SCSI ID
	(465, "UC*3",'''-- reserved'''), #-- reserved
	(468, "UL",'''b b9:IDE save mount on b8:IDE master mount on b7-0:SCSI ID7-0 mount on'''), #b b9:IDE save mount on b8:IDE master mount on b7-0:SCSI ID7-0 mount on
	(472, "UL",'''-- reserved'''), #-- reserved
	(473, "UC",'''0-98 top partition 1-99'''), #0-98 top partition 1-99
	(474, "UC*6",'''-- reserved'''), #-- reserved
	(480, "US",'''-- reserved'''), #-- reserved
	(482, "US",'''b b15-12:effect type1 favorite parameter1 b11-8:effect type1 favorite parameter2 b7-4:effect type1 favorite parameter3 b3-0:effect type1 favorite parameter4'''), #b b15-12:effect type1 favorite parameter1 b11-8:effect type1 favorite parameter2 b7-4:effect type1 favorite parameter3 b3-0:effect type1 favorite parameter4
	(484, "US*95",'''b effect type2-96 favorite parameters'''), #b effect type2-96 favorite parameters
	(674, "US*31",'''-- reserved'''), #-- reserved
	(736, "UC",'''-- reserved'''), #-- reserved
	(737, "UC",'''0-1 effect edit type'''), #0-1 effect edit type
	(738, "UC",'''0-4 knob2 control type'''), #0-4 knob2 control type
	(739, "UC",'''0-4 knob3 control type'''), #0-4 knob3 control type
	(740, "UC",'''0-4 knob4 control type'''), #0-4 knob4 control type
	(741, "UC",'''0-4 knob5 control type'''), #0-4 knob5 control type
	(742, "UC",'''0-5 assignable key function'''), #0-5 assignable key function
	(743, "UC",'''0-1 audition key function'''), #0-1 audition key function
	(744, "UC",'''0-1 page mode at mode change'''), #0-1 page mode at mode change
	(745, "UC",'''0-1 page mode at function change'''), #0-1 page mode at function change
	(746, "UC",'''0-1 note display type'''), #0-1 note display type
	(747, "UC*4",'''-- reserved'''), #-- reserved
	(751, "UC",'''0-3 end address display type'''), #0-3 end address display type
	(752, "UC",'''0-3 import view'''), #0-3 import view
	(753, "UC",'''0-1 knob1 type'''), #0-1 knob1 type
	(754, "UC*4",'''-- reserved'''), #-- reserved
	(758, "UC",'''0-2 sort type at sample select page'''), #0-2 sort type at sample select page
	(759, "UC",'''0-2 sort type at tree view page'''), #0-2 sort type at tree view page
	(760, "UC",'''0-2 sort type at samplebank page'''), #0-2 sort type at samplebank page
	(761, "UC",'''0-7 CD-R SCSI ID'''), #0-7 CD-R SCSI ID
	(762, "UC",'''0-4 CD-R write speed'''), #0-4 CD-R write speed
	(763, "UC*37",'''-- reserved'''), #-- reserved
	(800, "120byte",'''[Effect Parameter]*3 (rec effect1-3)'''), #[Effect Parameter]*3 (rec effect1-3)
	(920, "UC",'''0-3 record type'''), #0-3 record type
	(921, "UC",'''0-1 record sample mono/stereo'''), #0-1 record sample mono/stereo
	(922, "UC",'''0-4 record input'''), #0-4 record input
	(923, "UC",'''0-3 record frequency (*1)'''), #0-3 record frequency (*1)
	(924, "UC",'''0-5 pre trigger time'''), #0-5 pre trigger time
	(925, "UC",'''0-1 start trigger type'''), #0-1 start trigger type
	(926, "UC",'''0-1 stop trigger type'''), #0-1 stop trigger type
	(927, "UC",'''0-63 start edge level'''), #0-63 start edge level
	(928, "UC",'''0-63 stop edge level'''), #0-63 stop edge level
	(929, "SC",'''0-2 record map to'''), #0-2 record map to
	(930, "UC",'''-1,0-127 record key range low (*4)'''), #-1,0-127 record key range low (*4)
	(931, "UC",'''0-127,128 record key range high (*5)'''), #0-127,128 record key range high (*5)
	(932, "SC",'''0-127 record original key'''), #0-127 record original key
	(933, "UC",'''0-1 auto normalize on'''), #0-1 auto normalize on
	(934, "SC",'''-1,0-7 external control SCSI ID (*2)'''), #-1,0-7 external control SCSI ID (*2)
	(935, "UC",'''1-99 external control start track'''), #1-99 external control start track
	(936, "UC",'''1-99 external control start index'''), #1-99 external control start index
	(937, "UC",'''0-5 monitor output'''), #0-5 monitor output
	(938, "UC",'''0-127 monitor level'''), #0-127 monitor level
	(939, "UC",'''0-127 click level'''), #0-127 click level
	(940, "US",'''8000-15999 click tempo 80.00-159.99'''), #8000-15999 click tempo 80.00-159.99
	(942, "UC",'''1-15 click beat'''), #1-15 click beat
	(943, "UC",'''0-1 monitor on'''), #0-1 monitor on
	(944, "UC",'''0-1 record map manual/auto'''), #0-1 record map manual/auto
	(945, "UC",'''0-127 record map auto original key'''), #0-127 record map auto original key
	(946, "UC",'''0-1 record map key white/all'''), #0-1 record map key white/all
	(947, "UC*8",'''-- reserved'''), #-- reserved
	(955, "UC*16",'''-- reserved'''), #-- reserved
	(971, "UC",'''0-1 AD input gain line/mic'''), #0-1 AD input gain line/mic
	(972, "UC*3",'''-- reserved'''), #-- reserved
	(975, "UC*5",'''-- reserved'''), #-- reserved
	(980, "UC*8",'''-- reserved'''), #-- reserved
	(988, "UC*2",'''-- reserved'''), #-- reserved
	(990, "UC",'''0-1 bulk protect'''), #0-1 bulk protect
	(991, "UC",'''0-1 after touch disable'''), #0-1 after touch disable
	(992, "UC",'''0-1 control change disable'''), #0-1 control change disable
	(993, "UC",'''0-1 pitch bend disable'''), #0-1 pitch bend disable
	(994, "UC",'''-- reserved'''), #-- reserved
	(995, "UC",'''0-17 MIDI device number'''), #0-17 MIDI device number
	(996, "UC",'''0-1 SysEx receive port (reserved in A4000)'''), #0-1 SysEx receive port (reserved in A4000)
	(997, "UC*7",'''-- reserved'''), #-- reserved
	(1004, "224byte",'''[Sample Parameter]'''), #[Sample Parameter]
	(1228, "120byte",'''[Effect Parameter]*3 (effect1-3)'''), #[Effect Parameter]*3 (effect1-3)
	(1348, "16byte",'''reserved'''), #reserved
	(1364, "120byte",'''[Effect Parameter]*3 (effect4-6) (A5000 only)'''), #[Effect Parameter]*3 (effect4-6) (A5000 only)
	(1484, "16byte",'''[Control]*4 (program control1-4) 1500 US b b0:MIDI channel B01 controller reset... b15:MIDI channel B16 controller reset (A5000 only) 1502 US b b0:MIDI channel B01 note on normal/toggle... b15:MIDI channel B16 note on normal/toggle (A5000 only)'''), #[Control]*4 (program control1-4) 1500 US b b0:MIDI channel B01 controller reset... b15:MIDI channel B16 controller reset (A5000 only) 1502 US b b0:MIDI channel B01 note on normal/toggle... b15:MIDI channel B16 note on normal/toggle (A5000 only)
	(1504, "UC",'''b b2-0:effect connect (effect4-6)'''), #b b2-0:effect connect (effect4-6)
	(1505, "UC",'''0-12 AD in (L) output1'''), #0-12 AD in (L) output1
	(1506, "UC",'''0-127 AD in (L) level1'''), #0-127 AD in (L) level1
	(1507, "UC",'''0-12 AD in (L) output2'''), #0-12 AD in (L) output2
	(1508, "UC",'''0-127 AD in (L) level2'''), #0-127 AD in (L) level2
	(1509, "SC",'''+/ - 63 AD in R pan'''), #+/ - 63 AD in R pan
	(1510, "UC",'''0-12 AD in R output1'''), #0-12 AD in R output1
	(1511, "UC",'''0-127 AD in R level1'''), #0-127 AD in R level1
	(1512, "UC",'''0-12 AD in R output2'''), #0-12 AD in R output2
	(1513, "UC",'''0-127 AD in R level2'''), #0-127 AD in R level2
	(1514, "UC*16",'''0-127 program LFO step wave value1-16'''), #0-127 program LFO step wave value1-16
	(1530, "UC",'''b b2-0: step wave total steps, b4-3:step wave slope'''), #b b2-0: step wave total steps, b4-3:step wave slope
	(1531, "UC*9",'''-- reserved'''), #-- reserved
	(1540, "UC*8",'''-- reserved'''), #-- reserved
	(1548, "UC",'''b b0:AD in on, b2-1:AD in source, b5-3:effect connection(effect1-3), b7-6:program LFO sync'''), #b b0:AD in on, b2-1:AD in source, b5-3:effect connection(effect1-3), b7-6:program LFO sync
	(1549, "UC",'''b b2-0:program LFO cycle, b5-3:program LFO wave, b7-6:program LFO initial phase'''), #b b2-0:program LFO cycle, b5-3:program LFO wave, b7-6:program LFO initial phase
	(1550, "US",'''b b0:MIDI channel A01 controller reset... b15:MIDI channel A16 controller reset'''), #b b0:MIDI channel A01 controller reset... b15:MIDI channel A16 controller reset
	(1552, "US",'''b b0:MIDI channel A01 note on normal/toggle... b15:MIDI channel A16 note on normal/toggle'''), #b b0:MIDI channel A01 note on normal/toggle... b15:MIDI channel A16 note on normal/toggle
	(1554, "SC",'''±63 AD in (L) pan'''), #±63 AD in (L) pan
	(1555, "UC",'''-- reserved'''), #-- reserved
	(1556, "UC",'''-- reserved'''), #-- reserved
	(1557, "UC",'''-- reserved'''), #-- reserved
	(1558, "UC",'''-- reserved'''), #-- reserved
	(1559, "UC",'''0-127 program level'''), #0-127 program level
	(1560, "SC",'''-- reserved'''), #-- reserved
	(1561, "SC",'''-- reserved'''), #-- reserved
	(1562, "SC",'''±127 program transpose'''), #±127 program transpose
	(1563, "SC",'''-2,-1,0-32 program LFO reset MIDI channel (*6)'''), #-2,-1,0-32 program LFO reset MIDI channel (*6)
	(1564, "UC",'''0-3 program portamento type'''), #0-3 program portamento type
	(1565, "UC",'''0-127 program portamento rate'''), #0-127 program portamento rate
	(1566, "UC",'''0-127 program portamento time'''), #0-127 program portamento time
	(1567, "UC",'''0-127 S/H speed'''), #0-127 S/H speed
	(1568, "UC",'''25-250 program LFO tempo'''), #25-250 program LFO tempo
	(1569, "SC",'''-1,0-127 program LFO reset note (*7)'''), #-1,0-127 program LFO reset note (*7)
	(1570, "UC*10",'''-- reserved'''), #-- reserved
	(1580, "UC",'''0-1 sequence MIDI port B/A'''), #0-1 sequence MIDI port B/A
	(1581, "UC*15",'''-- reserved'''), #-- reserved
	(1596, "UC",'''0-1 DIG&OPT output 20bit/24bit'''), #0-1 DIG&OPT output 20bit/24bit
	(1597, "UC*2467",'''-- reserved'''), #-- reserved
)

control_function_map={
    0:'off',
    1:'portamento rate/time',
    2:'LFO S/H speed',
    3:'AD in L&R pan',
    4:'AD in L&R level',
    5:'program level',
    6:'effect1 output level',
    7:'effect1 pan',
    8:'effect1-parameter1',
    9:'effect1-parameter2',
    10:'effect1-parameter3',
    11:'effect1-parameter4',
    12:'effect1-parameter5',
    13:'effect1-parameter6',
    14:'effect1-parameter7',
    15:'effect1-parameter8',
    16:'effect1-parameter9',
    17:'effect1-parameter10',
    18:'effect1-parameter11',
    19:'effect1-parameter12',
    20:'effect1-parameter13',
    21:'effect1-parameter14',
    22:'effect1-parameter15',
    23:'effect1-parameter16',
    24:'effect2 output level',
    25:'effect2 pan',
    26:'effect2-parameter1',
    27:'effect2-parameter2',
    28:'effect2-parameter3',
    29:'effect2-parameter4',
    30:'effect2-parameter5',
    31:'effect2-parameter6',
    32:'effect2-parameter7',
    33:'effect2-parameter8',
    34:'effect2-parameter9',
    35:'effect2-parameter10',
    36:'effect2-parameter11',
    37:'effect2-parameter12',
    38:'effect2-parameter13',
    39:'effect2-parameter14',
    40:'effect2-parameter15',
    41:'effect2-parameter16',
    42:'effect3 output level',
    43:'effect3 pan',
    44:'effect3-parameter1',
    45:'effect3-parameter2',
    46:'effect3-parameter3',
    47:'effect3-parameter4',
    48:'effect3-parameter5',
    49:'effect3-parameter6',
    50:'effect3-parameter7',
    51:'effect3-parameter8',
    52:'effect3-parameter9',
    53:'effect3-parameter10',
    54:'effect3-parameter11',
    55:'effect3-parameter12',
    56:'effect3-parameter13',
    57:'effect3-parameter14',
    58:'effect3-parameter15',
    59:'effect3-parameter16',
    60:'effect1 width',
    61:'effect2 width',
    62:'effect3 width',
    63:'program LFO depth',
    64:'AD in L pan',
    65:'AD in R pan',
    66:'AD in L level',
    67:'AD in R level',
    68:'program control11 range',
    69:'program control12 range',
    70:'program control13 range',
    71:'program control14 range',
    72:'effect4-parameter1',
    73:'effect4-parameter2',
    74:'effect4-parameter3',
    75:'effect4-parameter4',
    76:'effect4-parameter5',
    77:'effect4-parameter6',
    78:'effect4-parameter7',
    79:'effect4-parameter8',
    80:'effect4-parameter9',
    81:'effect4-parameter10',
    82:'effect4-parameter11',
    83:'effect4-parameter12',
    84:'effect4-parameter13',
    85:'effect4-parameter14',
    86:'effect4-parameter15',
    87:'effect4-parameter16',
    88:'effect4 output level',
    89:'effect4 pan',
    90:'effect4 width',
    91:'effect5-parameter1',
    92:'effect5-parameter2',
    93:'effect5-parameter3',
    94:'effect5-parameter4',
    95:'effect5-parameter5',
    96:'effect5-parameter6',
    97:'effect5-parameter7',
    98:'effect5-parameter8',
    99:'effect5-parameter9',
    100:'effect5-parameter10',
    101:'effect5-parameter11',
    102:'effect5-parameter12',
    103:'effect5-parameter13',
    104:'effect5-parameter14',
    105:'effect5-parameter15',
    106:'effect5-parameter16',
    107:'effect5 output level',
    108:'effect5 pan',
    109:'effect5 width',
    110:'effect6-parameter1',
    111:'effect6-parameter2',
    112:'effect6-parameter3',
    113:'effect6-parameter4',
    114:'effect6-parameter5',
    115:'effect6-parameter6',
    116:'effect6-parameter7',
    117:'effect6-parameter8',
    118:'effect6-parameter9',
    119:'effect6-parameter10',
    120:'effect6-parameter11',
    121:'effect6-parameter12',
    122:'effect6-parameter13',
    123:'effect6-parameter14',
    124:'effect6-parameter15',
    125:'effect6-parameter16',
    126:'effect6 output level',
    127:'effect6 pan'}

	
control_function_map_s={
    0:'off',
    1:'pitch mod depth',
    2:'amp mod depth',
    3:'cutoff mod depth',
    4:'cutoff bias',
    5:'filter Q/width',
    6:'pan bias',
    7:'pitch bias',
    8:'level',
    9:'LFO speed',
    10:'LFO delay',
    11:'AEG attack rate',
    12:'AEG release rate',
    13:'PEG attack rate',
    14:'PEG release rate',
    15:'FEG attck rate',
    16:'FEG release rate',
    17:'pitch bend',
    18:'start address',
    19:'FEG level',
    20:'cutoff distance',
    21:'filter gain',
    22:'portamento rate/time',
    23:'AEG decay rate',
    24:'AEG sustain level',
    25:'FEG decay rate',
    26:'FEG init level',
    27:'FEG sustain level',
    28:'PEG decay rate',
    29:'PEG init level',
    30:'PEG sustain level',
    31:'sample control1 range',
    32:'sample control2 range',
    33:'sample control3 range',
    34:'sample control4 range',
    35:'sample control5 range',
    36:'sample control6 range'}

control_device_map={
    0:'Bank Select',
    1:'Modulation Wheel or Lever',
    2:'Breath Controller',
    3:'Undefined',
    4:'Foot Controller',
    5:'Portamento Time',
    6:'Data Entry MSB',
    7:'Channel Volume (formerly Main Volume)',
    8:'Balance',
    9:'Undefined',
    10:'Pan',
    11:'Expression Controller',
    12:'Effect Control 1',
    13:'Effect Control 2',
    14:'Undefined',
    15:'Undefined',
    16:'General Purpose Controller 1',
    17:'General Purpose Controller 2',
    18:'General Purpose Controller 3',
    19:'General Purpose Controller 4',
    20:'Undefined',
    21:'Undefined',
    22:'Undefined',
    23:'Undefined',
    24:'Undefined',
    25:'Undefined',
    26:'Undefined',
    27:'Undefined',
    28:'Undefined',
    29:'Undefined',
    30:'Undefined',
    31:'Undefined',
    32:'LSB for Control 0 (Bank Select)',
    33:'LSB for Control 1 (Modulation Wheel or Lever)',
    34:'LSB for Control 2 (Breath Controller)',
    35:'LSB for Control 3 (Undefined)',
    36:'LSB for Control 4 (Foot Controller)',
    37:'LSB for Control 5 (Portamento Time)',
    38:'LSB for Control 6 (Data Entry)',
    39:'LSB for Control 7 (Channel Volume, formerly Main Volume)',
    40:'LSB for Control 8 (Balance)',
    41:'LSB for Control 9 (Undefined)',
    42:'LSB for Control 10 (Pan)',
    43:'LSB for Control 11 (Expression Controller)',
    44:'LSB for Control 12 (Effect control 1)',
    45:'LSB for Control 13 (Effect control 2)',
    46:'LSB for Control 14 (Undefined)',
    47:'LSB for Control 15 (Undefined)',
    48:'LSB for Control 16 (General Purpose Controller 1)',
    49:'LSB for Control 17 (General Purpose Controller 2)',
    50:'LSB for Control 18 (General Purpose Controller 3)',
    51:'LSB for Control 19 (General Purpose Controller 4)',
    52:'LSB for Control 20 (Undefined)',
    53:'LSB for Control 21 (Undefined)',
    54:'LSB for Control 22 (Undefined)',
    55:'LSB for Control 23 (Undefined)',
    56:'LSB for Control 24 (Undefined)',
    57:'LSB for Control 25 (Undefined)',
    58:'LSB for Control 26 (Undefined)',
    59:'LSB for Control 27 (Undefined)',
    60:'LSB for Control 28 (Undefined)',
    61:'LSB for Control 29 (Undefined)',
    62:'LSB for Control 30 (Undefined)',
    63:'LSB for Control 31 (Undefined)',
    64:'Damper Pedal on/off (Sustain)	≤63 off, ≥64 on	---',
    65:'Portamento On/Off	≤63 off, ≥64 on	---',
    66:'Sostenuto On/Off	≤63 off, ≥64 on	---',
    67:'Soft Pedal On/Off	≤63 off, ≥64 on	---',
    68:'Legato Footswitch	≤63 Normal, ≥64 Legato	---',
    69:'Hold 2	≤63 off, ≥64 on	---',
    70:'Sound Controller 1 (default: Sound Variation)',
    71:'Sound Controller 2 (default: Timbre/Harmonic Intens.)',
    72:'Sound Controller 3 (default: Release Time)',
    73:'Sound Controller 4 (default: Attack Time)',
    74:'Sound Controller 5 (default: Brightness)',
    75:'Sound Controller 6 (default: Decay Time - see MMA RP-021)',
    76:'Sound Controller 7 (default: Vibrato Rate - see MMA RP-021)',
    77:'Sound Controller 8 (default: Vibrato Depth - see MMA RP-021)',
    78:'Sound Controller 9 (default: Vibrato Delay - see MMA RP-021)',
    79:'Sound Controller 10 (default undefined - see MMA RP-021)',
    80:'General Purpose Controller 5',
    81:'General Purpose Controller 6',
    82:'General Purpose Controller 7',
    83:'General Purpose Controller 8',
    84:'Portamento Control',
    85:'Undefined	---	---',
    86:'Undefined	---	---',
    87:'Undefined	---	---',
    88:'High Resolution Velocity Prefix',
    89:'Undefined	---	---',
    90:'Undefined	---	---',
    91:'Effects 1 Depth ',
    92:'Effects 2 Depth (formerly Tremolo Depth)	0-127	---',
    93:'Effects 3 Depth ',
    94:'Effects 4 Depth (formerly Celeste [Detune] Depth)	0-127	---',
    95:'Effects 5 Depth (formerly Phaser Depth)	0-127	---',
    96:'Data Increment (Data Entry +1) (see MMA RP-018)	N/A	---',
    97:'Data Decrement (Data Entry -1) (see MMA RP-018)	N/A	---',
    98:'Non-Registered Parameter Number (NRPN) - LSB',
    99:'Non-Registered Parameter Number (NRPN) - MSB',
    100:'Registered Parameter Number (RPN) - LSB*',
    101:'Registered Parameter Number (RPN) - MSB*',
    102:'Undefined	---	---',
    103:'Undefined	---	---',
    104:'Undefined	---	---',
    105:'Undefined	---	---',
    106:'Undefined	---	---',
    107:'Undefined	---	---',
    108:'Undefined	---	---',
    109:'Undefined	---	---',
    110:'Undefined	---	---',
    111:'Undefined	---	---',
    112:'Undefined	---	---',
    113:'Undefined	---	---',
    114:'Undefined	---	---',
    115:'Undefined	---	---',
    116:'Undefined	---	---',
    117:'Undefined	---	---',
    118:'Undefined	---	---',
    119:'Undefined	---	---',
    120:'[Channel Mode Message] All Sound Off	0	---',
    121:'[Channel Mode Message] Reset All Controllers ',
    122:'[Channel Mode Message] Local Control On/Off	0 off, 127 on	---',
    123:'[Channel Mode Message] All Notes Off	0	---',
    124:'[Channel Mode Message] Omni Mode Off (+ all notes off)	0	---',
    125:'[Channel Mode Message] Omni Mode On (+ all notes off)	0	---',
    126:'[Channel Mode Message] Mono Mode On (+ poly off, + all notes off)	',
    127:'[Channel Mode Message] Poly Mode On (+ mono off, +all notes off)	0	---'
	}
