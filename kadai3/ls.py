import os
import sys
import pwd
import stat
import grp
import datetime
import glob

mode = {'0':'---', '1':'--x', '2':'-w-', '3':'-wx', '4':'r--', '5':'r-x', '6':'rw-', '7':'rwx'}

def lscmd(options):
    current = '.'
    files = os.listdir(os.path.abspath(current))
    buff = ''
    for file in files:
        # -a option
        if 'a' not in options:
            if file.startswith("."):
                continue

        stat = os.stat(file)
        # -l option
        if 'i' in options:
            buff += "%s " % str(stat.st_ino)

        # -i option
        if 'l' in options:
            buff += "%s%s%s%s  %s %s  %s   %s%s %s" % (checkdir(file), conv(oct(stat.st_mode)[-3:][0:1:]),
            conv(oct(stat.st_mode)[-3:][1:2:]),conv(oct(stat.st_mode)[-3:][2:3:]),
            stat.st_nlink, pwd.getpwuid(stat.st_uid)[0], grp.getgrgid(stat.st_gid)[0],
            stat.st_size, 'B', convtime(stat.st_mtime))

        buff += file
        buff += '\r\n'

    print buff

def conv(num):
    for key, value in mode.items():
        if num is key:
            return value

def checkdir(file):
    if os.path.isdir(file):
        return 'd'
    else:
        return '-'

def convtime(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%b %d %H:%M')

if len(sys.argv) >= 2:
    options = sys.argv[1][1::] if sys.argv[1][0:1:].startswith('-') else ''
else:
    options = ''

lscmd(options)
