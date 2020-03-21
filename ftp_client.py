'''
FTP Client script for connecting and sending
files to an ftp server
'''

import ftplib
import os
import sys
__version__ = '1.0.0'

#connect to host
if(len(sys.argv) < 4):
    print('''
        Usage:
        python ftp_client.py [target IP] [user name] [password]
        ''');sys.exit()
else:
        pass

Ftp = ftplib.FTP("{}".format(sys.argv[1]))


#login
Ftp.login("{}".format(sys.argv[2],sys.argv[3]))

#Ftp.set_debuglevel(1)
print("""
        ================================
        U-F-T-P
        version:{}
        ================================
        """.format(__version__))
print()
print()
print()

class FTPp:
    
    def _action_(self):
        print("""
    \033[1;93m
    [+] choose action
    [1] change directory: <1> <dir>
    [2] list directory: <2>
    [3] Upload file: <3> <file> <upload_dir>
    [4] LogOut
    \033[1;92m
              """)
        print
        action = raw_input(":")

        if(action[0] == "1" and len(action) > 2):
                action = action.split()
                FTPp().Change_Dir(action[1])

        elif action[0] == "2":
                FTPp().List_Dir()
        elif action[0] == "3" and len(action) > 2:
                action = action.split()
                FTPp().Upload_File(action[1],action[2])
        else:
            pass

    def List_Dir(self):
        print(Ftp.dir())
        print()
        FTPp()._action_()

    def Change_Dir(self,dir):
        try:
            #Ftp.dir(dir)
            Ftp.cwd(str(dir))
            print( "[+] Directory changed to {}".format(str(Ftp.cwd(".").split()[1])))
            FTPp()._action_()
        except Exception, e:
            print e, dir
        FTPp()._action_()

    def LogOut(self):
        print( "[+] Loging Out..");Ftp.quit()

    def Upload_File(self,Lfile,Rfile):
        try:
                print("\033[1;95m [+]Uploading File {} to {}".format(Lfile,Rfile))
                file = open(Lfile,'r')
                Ftp.storbinary("STOR {}".format(os.path.basename(Rfile)),file)
                file.close()
                print( "\033[1;92m [+] Uploading complete...")
                return file.close()
        except Exception,e:
            print( "\033[1;96m [+]Could not Upload file...")
            print("\033[1;94m {}".format(e))



FTPp()._action_()
