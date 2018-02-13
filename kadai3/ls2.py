import os
import pwd
import grp
import time
import sys

argc = len(sys.argv)
if argc == 1:
        folder = os.getcwd()
elif argc == 2:
        folder = sys.argv[1]

files = os.listdir(folder)

for file in files:
        filesize = os.path.getsize(file)
        time = time.ctime(os.path.getatime(file))[4:16]
        user = pwd.getpwuid(os.stat(file).st_uid).pw_name
        group = grp.getgrgid(os.stat(file).st_gid).gr_name
        ntlink = os.stat(file).st_nlink
        print ntlink, user, group, filesize, time, file
