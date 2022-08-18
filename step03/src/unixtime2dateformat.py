import sys
from datetime import datetime, timedelta, timezone
import traceback

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

def main():
    """メイン処理

    引数のunixtimeを日付フォーマットに変換し、標準出力する。

    Args:
        なし
    Returns:
        なし
    """
    # 引数から値を取得
    unixtime = get_unixtime(sys.argv)
    if unixtime < 0:
        return

    # 変換
    date = unix2datetime(unixtime)

    # 結果を標準出力
    print(date.strftime(DATE_FORMAT))


def get_unixtime(argv):
    """引数のunixtime取得

    コマンド第2引数のunixtimeを取得しIntへ型変換を行う

    Args:
        argv (list): コマンド引数のlist

    Returns:
        int: 不正な値の場合、-1 それ以外は 0以上の整数
        ※不正な値は以下
        * 第2引数が省略されている場合
        * int型変換できない場合
        * 0未満の値が指定された場合

    Examples:
        >>> print(get_unixtime(100))
        100
    """
    try:
        unixtime_str = argv[1]
        unixtime = int(unixtime_str)
        if unixtime < 0:
            print(f'unixtimeは0以上の整数を指定してください。value = {unixtime}')
            return -1

        return unixtime
    except IndexError:
        print(f'引数を指定してください。value = {argv}\n', traceback.format_exc())
        return -1
    except ValueError:
        print(f'引数の型が不正です。value = {argv[1]}\n', traceback.format_exc())
        return -1


def unix2datetime(unixtime):
    """unixtimeをdatetime型に変換する

    unixtimeをtimezone JST の datetime型に変換する

    Args:
        unixtime (int): unixtimeを表す数値

    Returns:
        datetime: unixtimeを変換した結果。timezoneは JST

    Examples:
        >>> unix2datetime(100)
        datetime.datetime(1970, 1, 1, 9, 1, 40, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST'))
    """
    # timezoneを指定して日付型に変換
    jst = timezone(timedelta(hours=9), 'JST')
    date = datetime.fromtimestamp(unixtime, jst)
    return date


if __name__ == '__main__':
    main()
