# Stop Drop and Roll
## Description
The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...
## Approach
I used this script to automate response from the nc
```python
from pwn import *

r = remote('83.136.254.37', 53505)

r.recvuntil(b'(y/n) ')

r.sendline(b'y')

r.recvuntil(b'\n')

tries = 0

replacements = {
    ", ": "-",
    "GORGE": "STOP",
    "PHREAK": "DROP",
    "FIRE": "ROLL"
}

while True:
    try:
        got = r.recvline().decode()
        
        for key, value in replacements.items():
            got = got.replace(key, value)
        
        payload = got.strip()
        r.sendlineafter(b'What do you do?', payload.encode())
        tries += 1
        log.info(f'{tries}: {payload}')
    except EOFError:
        log.success(got.strip())
        r.close()
        break
```
## Flag 
```
HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}
```
