# Q23.[Reversing]またやらかした！
またprintf（）をし忘れたプログラムが見つかった。
とある暗号を解くプログラムらしい…


## Solution
例によってIDAを用いて配布されたプログラムを確認する。

`zixnbo|kwxt88d`の文字列をどうやら操作しているようで、各々の文字を`19h`とXORの結果を別の変数に格納している。
従って、文字列の操作を行うループ後にブレイクポイントを貼り、処理後のスタックの状態を確認してみる。

```
$ gdb rev200
gdb-peda$ b *0x08048497
Breakpoint 1 at 0x8048497
gdb-peda$ run
Starting program: /home/kali/work/cpawctf-writeup/level3/q23/rev200 
[----------------------------------registers-----------------------------------]
EAX: 0xd ('\r')
EBX: 0xffffcff8 --> 0x63 ('c')
ECX: 0x0 
EDX: 0x7d ('}')
ESI: 0x1 
EDI: 0xffffd030 --> 0x0 
EBP: 0xffffd038 --> 0x0 
ESP: 0xffffcfb0 --> 0x0 
EIP: 0x8048497 (<main+170>:     mov    eax,0x0)
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x804848d <main+160>:        add    DWORD PTR [ebp-0x80],0x1
   0x8048491 <main+164>:        cmp    DWORD PTR [ebp-0x80],0xd
   0x8048495 <main+168>:        jle    0x804847a <main+141>
=> 0x8048497 <main+170>:        mov    eax,0x0
   0x804849c <main+175>:        sub    esp,0xffffff80
   0x804849f <main+178>:        pop    ebx
   0x80484a0 <main+179>:        pop    edi
   0x80484a1 <main+180>:        pop    ebp
[------------------------------------stack-------------------------------------]
0000| 0xffffcfb0 --> 0x0 
0004| 0xffffcfb4 --> 0x1 
0008| 0xffffcfb8 --> 0xe 
0012| 0xffffcfbc --> 0x19 
0016| 0xffffcfc0 --> 0x7a ('z')
0020| 0xffffcfc4 --> 0x69 ('i')
0024| 0xffffcfc8 --> 0x78 ('x')
0028| 0xffffcfcc --> 0x6e ('n')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x08048497 in main ()
gdb-peda$ telescope 50
0000| 0xffffcfb0 --> 0x0 
0004| 0xffffcfb4 --> 0x1 
0008| 0xffffcfb8 --> 0xe 
0012| 0xffffcfbc --> 0x19 
0016| 0xffffcfc0 --> 0x7a ('z')
0020| 0xffffcfc4 --> 0x69 ('i')
0024| 0xffffcfc8 --> 0x78 ('x')
0028| 0xffffcfcc --> 0x6e ('n')
0032| 0xffffcfd0 --> 0x62 ('b')
0036| 0xffffcfd4 --> 0x6f ('o')
0040| 0xffffcfd8 --> 0x7c ('|')
0044| 0xffffcfdc --> 0x6b ('k')
0048| 0xffffcfe0 --> 0x77 ('w')
0052| 0xffffcfe4 --> 0x78 ('x')
0056| 0xffffcfe8 --> 0x74 ('t')
0060| 0xffffcfec --> 0x38 ('8')
0064| 0xffffcff0 --> 0x38 ('8')
0068| 0xffffcff4 --> 0x64 ('d')
0072| 0xffffcff8 --> 0x63 ('c')
0076| 0xffffcffc --> 0x70 ('p')
0080| 0xffffd000 --> 0x61 ('a')
0084| 0xffffd004 --> 0x77 ('w')
0088| 0xffffd008 --> 0x7b ('{')
0092| 0xffffd00c --> 0x76 ('v')
0096| 0xffffd010 --> 0x65 ('e')
0100| 0xffffd014 --> 0x72 ('r')
0104| 0xffffd018 --> 0x6e ('n')
0108| 0xffffd01c --> 0x61 ('a')
0112| 0xffffd020 --> 0x6d ('m')
0116| 0xffffd024 --> 0x21 ('!')
0120| 0xffffd028 --> 0x21 ('!')
0124| 0xffffd02c --> 0x7d ('}')
0128| 0xffffd030 --> 0x0 
0132| 0xffffd034 --> 0x80482f0 (<_start>:       xor    ebp,ebp)
0136| 0xffffd038 --> 0x0 
0140| 0xffffd03c --> 0xf7dcf905 (<__libc_start_main+229>:       add    esp,0x10)
0144| 0xffffd040 --> 0x1 
0148| 0xffffd044 --> 0xffffd0e4 --> 0xffffd2b1 ("/home/kali/work/cpawctf-writeup/level3/q23/rev200")
0152| 0xffffd048 --> 0xffffd0ec --> 0xffffd2e3 ("CLUTTER_IM_MODULE=ibus")
0156| 0xffffd04c --> 0xffffd074 --> 0x0 
0160| 0xffffd050 --> 0xffffd084 --> 0xa8423a1c 
0164| 0xffffd054 --> 0xf7ffdb98 --> 0xf7ffdb30 --> 0xf7fc33f0 --> 0xf7ffd9d0 --> 0x0 
0168| 0xffffd058 --> 0xf7fc3420 --> 0x8048247 ("GLIBC_2.0")
0172| 0xffffd05c --> 0xf7f9c000 --> 0x1ead6c 
0176| 0xffffd060 --> 0x1 
0180| 0xffffd064 --> 0x0 
0184| 0xffffd068 --> 0xffffd0c8 --> 0xffffd0e4 --> 0xffffd2b1 ("/home/kali/work/cpawctf-writeup/level3/q23/rev200")
0188| 0xffffd06c --> 0x0 
0192| 0xffffd070 --> 0xf7ffd000 --> 0x31f3c 
0196| 0xffffd074 --> 0x0 
```

予想通り、操作後の文字列はFlagであった。

## Answer
cpaw{vernam!!}