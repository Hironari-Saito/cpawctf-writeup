# Q20.[Crypto]Block Cipher

与えられたC言語のソースコードを読み解いて復号してフラグを手にれましょう。

暗号文：cpaw{ruoYced_ehpigniriks_i_llrg_stae}

## Solution

与えられた`crypto100.c`の中身を確認してみる。


### About argv
第一引数は与えられたflag、第二引数は何らかの数字であることがわかる。
```
int key = atoi(argv[2]);
const char* flag = argv[1];
```

### main loop
最初のループは、開始点をkey - 1とし、ループの度にkeyの値を加えていき、`flag`の文字数を超えた場合にループを終了する。
今回の暗号は、`ruoYced_ehpigniriks_i_llrg_stae`の文字数で`31文字`であることから、keyの最大値は`32`である（それを超えるとそもそもループしないため)。

どんな感じのループになるのかの例

```
key: 1
0 1 2 3 4 5 .....
key: 2
1 3 5 7 9 11 .......
key: 3
2 5 8 11 14 .......
...
```

次のループは、開始点をiとし、ループの度に値を1つ引いていき、`i - key + 1`より小さくなった場合にループを終了する。その間flag[j]を出力する。
開始点が外側のループのiの値を受け取っており、`i - key + 1`より小さい場合、値を出力しないことからkeyの最小値は`1`である(それより小さいとループの対象外となる)

このループでは、開始点`i`から`i - key + 1`の値だけ、位置を逆にして出力する。

どんな感じのループになるのかの例
```
key: 2
flag[1] flag[0] flag[3] flag[2] flag[5] flag[4]
key: 3
flag[2] flag[1] flag[0] flag[5] flag[4] flag[3]
...
```

printf("cpaw{");
for(i = key - 1; i <= strlen(flag); i+=key)
  for(j = i; j>= i - key + 1; j--) 
    printf("%c", flag[j]);
printf("}");
```


### 実行
どのように処理されるのはわかったので、コンパイルしてkeyを1から31まで出力させてみる。

```
gcc crypto100.c -o crypto100.exe
./exec.sh
```

この中で意味が通るものがFlagであった。

## Answer
cpaw{Your_deciphering_skill_is_great}
