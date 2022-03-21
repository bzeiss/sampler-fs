
# Sample disk images of A3000 disk

At the moment one disk image which consists of 8GB disk (maximum size of the AxK samplers)
just after partitioning in the sampler (8 partitions á 1GB)

The disk was zeroed before installing in the A3K to allow for good compression of the image.
It can be read directly as a stream from python with the gzip module or encoding. So no need to waste disk space with the expannded file.




## Usage/Examples

```bash
host$ czat A3K_Disk_partioned.img.gz | hexdump -c | less
```
```ansi
00000000  59 41 4d 41 48 41 5f 64  65 76 33 00 00 00 00 00  |YAMAHA_dev3.....|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000080  d8 4c 00 0d 4a e8 00 00  00 00 03 18 03 a8 00 00  |.L..J...........|
00000090  00 00 03 18 03 a8 00 00  00 00 00 0d 00 00 02 00  |................|
000000a0  01 0f 59 c8 00 00 00 00  00 00 00 03 00 1f ff fe  |..Y.............|
000000b0  00 20 00 02 00 1f ff fe  00 40 00 01 00 1f ff fe  |. .......@......|
000000c0  00 60 00 00 00 1f ff fe  00 7f ff ff 00 1f ff fe  |.`..............|
000000d0  00 9f ff fe 00 1f ff fe  00 bf ff fd 00 1f ff fe  |................|
000000e0  00 df ff fc 00 1f ff fe  00 00 00 00 00 00 00 00  |................|
000000f0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000200  59 41 4d 41 48 41 5f 64  65 76 33 00 00 00 00 00  |YAMAHA_dev3.....|
00000210  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000280  d8 4c 00 0d 4a e8 00 00  00 00 03 18 03 a8 00 00  |.L..J...........|
00000290  00 00 03 18 03 a8 00 00  00 00 00 0d 00 00 02 00  |................|
000002a0  01 0f 59 c8 00 00 00 00  00 00 00 03 00 1f ff fe  |..Y.............|
000002b0  00 20 00 02 00 1f ff fe  00 40 00 01 00 1f ff fe  |. .......@......|
000002c0  00 60 00 00 00 1f ff fe  00 7f ff ff 00 1f ff fe  |.`..............|
000002d0  00 9f ff fe 00 1f ff fe  00 bf ff fd 00 1f ff fe  |................|
000002e0  00 df ff fc 00 1f ff fe  00 00 00 00 00 00 00 00  |................|
000002f0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
```


