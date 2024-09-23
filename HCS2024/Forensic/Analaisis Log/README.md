# Analisis Log
## Description
Baru juga nge-deploy website, ehhh 5 menit kemudian udah kena hack. Tolong bantu aku untuk menganalisis log ini dan jawablah pertanyaan-pertanyaan yang telah disediakan

Author: daffainfo

nc 178.128.218.40 3001
## Approach
To get flag from this challange, we must answer each question. 
### Question 1
Pertanyaan: Pukul berapa penyerang memulai melakukan fuzzing?
To solve this, just search `fuzz` in the log file. The date with the fuzz appearing first is the answer
```
06/Sep/2024:15:51:02
```
### Question 2
Pertanyaan: Nama plugin WordPress apa yang memiliki kerentanan yang dimanfaatkan oleh penyerang?
To solve this, search `200` in the log file after the first search result. 
```
canto
```
### Question 3
Pertanyaan: CVE apa yang digunakan oleh penyerang untuk mengeksploitasi server?
To solve this, search in the internet with this format `plugin-canto WordPress vulnerability CVE`. The answer is
```
CVE-2023-3452
```
### Question 4
Pertanyaan: Alamat IP apa saja yang dimiliki oleh penyerang? (Urutkan IP yang terkecil ke yang terbesar)
We already know the one of the attacker IP is 182.1.91.201 but if we answer only this its false. So we search other attacker ip. In here 
![attacker2 log](https://github.com/user-attachments/assets/6231ef78-5b30-466e-ab7b-2e8e27e7c7d7)
68.183.26.104 is the IP address of the server hosting the malicious script. The attacker is using this server to deliver the payload. If we try these ip, it will be true.
```
68.183.26.104,182.1.91.201
```
### Question 5
Pertanyaan: File apa yang diperiksa isinya oleh penyerang, berikan full pathnya?
Diperiksa means attacker doing some activity like cat, echo, etc. If we search `echo` in the log, we will get this
![path ans](https://github.com/user-attachments/assets/8ce958bf-3f22-4d49-9f6c-4012b989bb59)
I use copilot to translate it and get this
```
echo 'cG5nIC9yZ3AvY25mZmpx' | base64 -d | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
If we try that, we will get 
```
cat /etc/passwd
```
### Question 6
Pertanyaan: Apa nama file yang ditaruh oleh penyerang ke dalam server?
In the last line of the log file
![lastline](https://github.com/user-attachments/assets/cc9434a5-cb03-48dc-9b40-fabc8ec1dce5)
If we decode this, we get like this
```
echo 'cnB1YiAnPD9jdWMgcnB1YiAiVWJ5biBmcnpobmFsbiwgZnJ6YnRuIG92Zm4gem5maHggVVBGIExOTk4iID8+JyA+PiAvaW5lL2pqai91Z3p5L3FoZmdueF8zMjMxMi5jdWM=' | base64 -d | tr 'A-Za-z' 'N-ZA-Mn-za-m' | bash
```
And if we execute it in terminal, we will get 
![lastline2](https://github.com/user-attachments/assets/27627591-989c-4b40-a039-219e3dbb3441)
As we can see, the answer is
```
dustak_32312.php
```
After we answers all of those, we will get the flag.
## Flag
```
HCS{asik_lho_belajar_analisis_log_server}
```


