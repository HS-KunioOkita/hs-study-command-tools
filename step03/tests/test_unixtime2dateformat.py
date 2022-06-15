import pytest
import sys

from datetime import datetime, timezone, timedelta
from src.unixtime2dateformat import main, unix2datetime, get_unixtime



# 正常系を含む境界値試験
@pytest.mark.parametrize(('argv', 'expected'),[
    (['', '-100'], -1),
    (['', '-1'], -1),
    (['', '0'], 0),
    (['', '1'], 1),
    (['', '100'], 100),
])
def test_get_unixtime(argv, expected):
    assert get_unixtime(argv) == expected

# 引数に指定されていない場合、-1が返却される
def test_get_unixtime_indexerror(capfd):
    # 戻り値チェック
    assert get_unixtime(['']) == -1
    # 標準出力内容チェック
    out, err = capfd.readouterr()
    assert out.startswith("引数を指定してください。value = ['']") == True
    assert err == ''

# 引数に数値以外が指定された場合、-1が返却される
def test_get_unixtime_valueerror(capfd):
    # 戻り値チェック
    assert get_unixtime(['', 'abc']) == -1
    # 標準出力内容チェック
    out, err = capfd.readouterr()
    assert out.startswith("引数の型が不正です。value = abc") == True
    assert err == ''

# 正常系確認
def test_unix2datetime():
    assert unix2datetime(1) == datetime(1970, 1, 1, 9, 0, 1, tzinfo=timezone(timedelta(seconds=32400), 'JST'))


# 正常系確認
def test_main(capfd, mocker):
    test_argments = ['', '100']
    mocker.patch('sys.argv', return_value=test_argments)
    main()
    out, err = capfd.readouterr()
    assert out == '1970-01-01T09:00:01+0900\n'
    assert err == ''

# 不正な値確認
def test_main_invalid_argment(capfd, mocker):
    test_argments = ['', 'a']
    mocker.patch('sys.argv', return_value=test_argments)
    main()
    out, err = capfd.readouterr()
    #assert out.startswith("引数の型が不正です。value = a") == True
    #assert err == ''
