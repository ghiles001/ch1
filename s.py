import os
from qrtools import QR

i = 1

for i in range(1000):
    os.rename("pswd.png", str(i)+'pswd.png')
    myqr = QR(filename = i+'pswd.png')
    myqr.decode()
    pswd = myqr.data
    print(pswd)
    os.rename("unzipmev2.zip", str(i)+"unzipmev2.zip")

    cmd = "unzip -P "+str(pswd)+" "+str(i)+'unzipmev2.zip'

    os.system(md)

    os.remove(str(i)+'unzipmev2.zip')
    os.remove(str(i)+"pswd.png")

