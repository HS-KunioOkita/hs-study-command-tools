import sys
from unittest.mock import patch

from unixtime2dateformat_simple import main


# 正常系確認
def test_main(capfd, mocker):
    test_argments = ['', '1']
    with patch.object(sys, 'argv', test_argments):
        main()
        out, err = capfd.readouterr()
        assert out == '1970-01-01T09:00:01+0900\n'
        assert err == ''
