# Character
## Description
Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!
## Approch
i used this script to solve this challange
```python
from pwn import *

r = remote('83.136.254.47', 32433)
index = 0
flag = ""

while True:
    try:
        r.recvuntil(b'Which character (index) of the flag do you want? Enter an index: ')
        r.sendline(str(index).encode())
        got = r.recvline().decode()
        print(f"Received: {got}")
        character = got.split(": ")[1].strip()
        flag += character
        index += 1

        if "}" in got:
            r.close()
            break
    except EOFError:
        r.close()
        break

print("The flag is: ",flag)
```
## Flag
```
HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}
```
