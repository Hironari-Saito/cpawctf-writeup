# Q19.[Misc]Image!
Find the flag in this zip file.

## Solution
zipを解凍しようと試みるが、できない。そもそもzipなのか調べるためにfileコマンドを実行する
```
$ file misc100.zip 
misc100.zip: OpenDocument Drawing
```

OpenDocument Drawingという形式らしいので、拡張子を変更したもののようだ。
Googleでこの形式の拡張子を調べると.odgみたいなので、拡張子を変更する。
以下のサイトで.odgをpdfに変換してみる。
https://www.zamzar.com/convert/odg-to-pdf/

FLAGの中身が黒で塗りつぶされているが、コピー&ペーストでそのFLAGを獲得できる。
## Answer
cpaw{It_is_fun__isn't_it?}
