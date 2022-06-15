import sys
from datetime import datetime, timedelta, timezone


def main():
    unixtime = int(sys.argv[1])
    jst = timezone(timedelta(hours=9), 'JST')
    date = datetime.fromtimestamp(unixtime, jst)
    print(date.strftime('%Y-%m-%dT%H:%M:%S%z'))


if __name__ == '__main__':
    main()