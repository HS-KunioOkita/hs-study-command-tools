## Hellow World

### Python コマンド実行

```
$ python xxx.py
```

### print と write
Pythonでは標準出力するための方法として、`print` と `write` があります。  
両者の違いは、
1. 文末に改行が入るかどうか  
`print`は改行入るが、`write` は入らない。  
(print 関数では内部的に write を利用している。)
2. オブジェクトなどの出力に対応しているかどうか  
`print`はオブジェクトを引数に取れるが、`write`は文字列のみ許容する

```
hello_world = "Hello World!"
print(hello_world)
sys.stdout.write(hello_world)

object_sample = {"abc": "def"}
# これは大丈夫
print(object_sample)
# これはエラーになる
sys.stdout.write(object_sample)
# こんなかんじで stringに変換する必要あり
sys.stdout.write(str(object_sample))
```

通常は、`print` を使えば良さそうです。


