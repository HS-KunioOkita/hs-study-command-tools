## Hellow World

### print と write
Pythonでは標準出力するための方法として、`print` と `write` があります。  
両者の違いは、文末に改行が入るかどうかです。  
(print 関数では内部的に write を利用している。)

```
hello_world = "Hello World!"
print(hello_world)
sys.stdout.write(hello_world)
```

通常は、`print` を使えば良さそうです。