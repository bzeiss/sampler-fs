
# Set of files to work on the midi dumps

The structure of the midi sysex could be a base to explore the SFS (filesystem) of the AxK samplers.
These scripts are mainly used interactively to explore aspects of the data.

Mainly python2 at the moment. Just made available as starting point and need a good overhaul.
## Usage/Examples

```bash
host$ python -i yamaha_sysex.py
```
```python

>>> for offset,format,description in Easy_Edit_Parameter_Block:
...     print(offset,format,description)
... 
(0, 'UC*16', 'c assigned sample(bank) name')
(16, 'UL', '-- reserved')
(20, 'UC', 'assigned object type (sample:16, sample bank:17)')
(21, 'SC', '-1,0-32 MIDI receive channel assign ( -1:"=sample", 0-15:A01-A16, 16:basic receive channel, 17-32:B01-16(A5000 only))')
(22, 'SC', '\xc2\xb1127 level offset')
(23, 'SC', '\xc2\xb1127 velocity sensitivity')
(24, 'SC', '\xc2\xb1127 pan offset')
(25, 'SC', '\xc2\xb1127 velocity x-fade high offset')
(26, 'SC', '\xc2\xb1127 fine tune offset')
(27, 'SC', '\xc2\xb1127 velocity x-fade low offset')
(28, 'SC', '\xc2\xb1127 coarse tune offset')
(29, 'SC', '-1,0-12 output1 (*5)')
(30, 'UC', '0-127 key limit high ( >=low)')
(31, 'UC', '0-127 key limit low ( <=high)')
(32, 'SC', '\xc2\xb1127 key range shift')
(33, 'UC', '0-127 velocity limit high ( >=low)')
(34, 'UC', '0-127 velocity limit low ( <=high)')
(35, 'UC', 'b b0:portamento, b2:mono mode, b4:key x-fade on,b6:reserved (*3)')
(36, 'SC', '-1,0-16 alternate group number (*2)')
(37, 'SC', '\xc2\xb1127 AEG attack rate offset')
(38, 'SC', '\xc2\xb1127 AEG decay rate offset')
(39, 'SC', '\xc2\xb1127 AEG release rate offset')
(40, 'SC', '-1,0-12 output2 (*5)')
(41, 'SC', '\xc2\xb1127 filter cutoff offset')
(42, 'SC', '\xc2\xb163 filter gain offset')
(43, 'SC', '\xc2\xb131 filter Q/width offset')
(44, 'SC', '\xc2\xb1127 cutoff distance offset')
(45, 'SC', '-- reserved')
(46, 'SC', '-- reserved')
(47, 'SC', '\xc2\xb1127 output1 level offset')
(48, 'SC', '-- reserved')
(49, 'SC', '-- reserved')
(50, 'SC', '\xc2\xb1127 output2 level offset')
(51, 'UC', '0-1 MIDI control on')
(52, 'UC', '-- reserved')
(53, 'UC*3', '-- reserved')
>>> 

```


