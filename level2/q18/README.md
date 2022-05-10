# Q18.[Forensic]leaf in forest
このファイルの中にはフラグがあります。探してください。
フラグはすべて小文字です！


## Solution
1. 提供されたファイルを確認すると`lovelive!`の文字列の中にちらちらと異なる文字列があることが確認できる。
```
strings misc100
```
中にあるlovelive!の文字列を削除してみると、フラグっぽい文字列があったので、以下のコマンドでごにょごにょしてフラグを取得する。

`strings misc100 | tr -d lovelive! | tr -s 'A-Z{}' | tr A-Z a-z`

## Answer
cpaw{mgrep}
