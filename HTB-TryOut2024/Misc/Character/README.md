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
