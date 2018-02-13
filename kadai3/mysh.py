import os
import datetime
from cmd import Cmd

class MyShell(Cmd):
    prompt = "mysh> "

    def __init__(self):
        Cmd.__init__(self)

    def do_pwd(self, arg):
        print os.getcwd()

    def do_cd(self, arg):
        if len(arg) <= 0:
            os.chdir('/Users/Yosuke/')
        else:
            os.chdir(arg)

    def do_date(self, arg):
        now = datetime.datetime.now()
        print now.strftime("%a %b   %d  %H:%M:%S  %Z %Y")

    def do_exit(self, arg):
        print 'bye'
        return True

if __name__ == '__main__':
    MyShell().cmdloop()
