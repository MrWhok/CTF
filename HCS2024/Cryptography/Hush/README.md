# Hush
## Description
Mari belajar hash

Suatu algoritma untuk mengonversi data sesuai format tertentu, yang tidak bisa dikembalikan ke data aslinya. data yang sama seharusnya memiliki hasil hash yang sama, dan data yang berbeda meskipun 1 byte seharusnya memiliki hasil hash yang berbeda. fungsi :

Mengamankan data tersimpan dengan format yang tidak bisa dibaca i.e "password"
Sebagai signature integritas suatu file/data
Dll.
Author: idzoyy
## Aproach
I used bruteforoce to solve this challange, trying every possible order. Hash every order of the parts until it have same value with target hash.
```python
import itertools
import hashlib

target_hash = '83106e2e86716463f5d7e6363473559c'

parts = ['dc80', '5590', '5f8a', '14e}', 'a6cc', 'c5d8', 'HCS{', 'f659', '7a50']

def find_correct_order(parts, target_hash):
    permutations = itertools.permutations(parts)
    
    for perm in permutations:
        flag = ''.join(perm)
        
        flag_hash = hashlib.md5(flag.encode()).hexdigest()
        
        if flag_hash == target_hash:
            return flag

correct_flag = find_correct_order(parts, target_hash)

print(f"The flag is: {correct_flag}")
```
## Flag
`HCS{c5d87a505f8a5590a6ccf659dc8014e}`
