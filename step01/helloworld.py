import sys

hello_world = "Hello World!"
# print関数
print(hello_world)
# write関数(標準出力ファイルにwriteする)
sys.stdout.write(hello_world)
sys.stdout.write("\n")

object_sample = {"abc": "def"}
print(object_sample)
# sys.stdout.write(object_sample)
sys.stdout.write(str(object_sample))
sys.stdout.write("\n")
