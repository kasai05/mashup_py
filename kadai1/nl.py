# -*- coding:utf-8 -*-

import sys, re

def disp_lines(lines):
    count = 0
    for line in lines:
        count += 1
        print str(count) + ' ' + re.sub('[\r\n]', '', line)

if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1], "rU")
        disp_lines(f.readlines())
        f.close()
    except IOError as e:
        sys.exit("wc: %s: No such file or directory" % (sys.argv[1]))
else:
    disp_lines(sys.stdin.readlines())
