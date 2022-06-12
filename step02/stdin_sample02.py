import sys


def main():
    str = input('入力してください>>')
    print("入力値：{}".format(str))


def main_use_readline():
    print('入力してください(readline)>>')
    str = sys.stdin.readline()
    print("入力値：{}".format(str))


if __name__ == "__main__":
    main()
    main_use_readline()
