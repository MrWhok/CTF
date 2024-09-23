# Logic Gate
## Description
Decrypt ciphertext untuk mendapatkan flag

Author: ryuk

## Approach 
We reversed the order of the encryption.
```python
def decrypt(ciphertext):
    decrypted = []
    for c in ciphertext:
        a = (c >> 8) & 0xFF  
        b = c & 0xFF         
        
        x = b + a

        if x == 0:
            decrypted.append(0)
            continue

        if a == 0:
            y = 0  
        else:
            y = a  

        decrypted.append(x)

    return bytes(decrypted)

ciphertext = [16392, 16897, 20993, 10323, 27136, 8532, 370, 5216, 17945, 4200, 9546, 4194, 20240, 18465, 29696, 27665]
decrypted_flag = decrypt(ciphertext)
print(decrypted_flag)
```
## FLag
![logic gate](https://github.com/user-attachments/assets/ea04c992-050a-4124-9ddd-91b5ca043b94)


