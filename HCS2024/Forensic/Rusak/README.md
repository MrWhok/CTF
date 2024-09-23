# Rusak
## Description
Dikasih file dari temen eh malah gabisa dibuka, kira-kira kenapa yak?

Author: daffainfo
## Approach
If i using `file` command to see what this file type is, the output will be `data`. So i tried to use `xxd`. <br>
![broken-flag](https://github.com/user-attachments/assets/fd0f33fa-6269-459b-99bc-93a165e95a9e) <br>
As we can see, bytes of GN is reversed. But if we only swap GN bytes it doesnt mean anything. So i think bytes of P. is also reversed. Not only that IHDR and IDAT are reversed to. 
So, by assuming all of 2 bytes are reversed, i used this code to reverse all of those.
```python
def swap_bytes(hex_data):
    swapped = bytearray()
    for i in range(0, len(hex_data), 2):
        swapped.append(hex_data[i+1])
        swapped.append(hex_data[i])
    return swapped

# Read the 'broken_flag' file
with open('broken_flag', 'rb') as f:
    broken_flag_data = f.read()

# Swap the bytes
swapped_data = swap_bytes(broken_flag_data)

# Write the result to a new file
with open('fixed_flag4', 'wb') as f:
    f.write(swapped_data)

print("The bytes have been swapped and the result is written to 'fixed_flag.png'.")
```
The output of this will be an image of the flag.
## Flag
![fixed_flag4](https://github.com/user-attachments/assets/d1f143c1-96c6-46e8-b4cc-34d62c60134b)

