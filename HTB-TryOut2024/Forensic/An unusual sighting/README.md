# An unusual sighting
## Description
As the preparations come to an end, and The Fray draws near each day, our newly established team has started work on refactoring the new CMS application for the competition. However, after some time we noticed that a lot of our work mysteriously has been disappearing! We managed to extract the SSH Logs and the Bash History from our dev server in question. The faction that manages to uncover the perpetrator will have a massive bonus come competition!
## Approach
### Question 1
What is the IP Address and Port of the SSH Server (IP:PORT) <br>
The answer is in this line `[2024-01-28 15:24:23] Connection from 100.72.1.95 port 47721 on 100.107.36.130 port 2221 rdomain ""`, from that we can get
```
100.107.36.130:2221
```
### Question 2
What time is the first successful Login <br> 
We can check first Accepted output from the sshd.log. We can use this command in terminal
```
cat sshd.log | grep Accepted
```
and the output is
![image](https://github.com/user-attachments/assets/fab92a9d-b086-435b-9898-ac6e547ead35)
So the answer is the first Accepted output
```
2024-02-13 11:29:50
```
### Question 3
What is the time of the unusual Login <br>
We can check several indicator of the unsual login, like who is the user?what time was that user login? Is it using bruteforce?etc. After i investigate it, i get this 
![image](https://github.com/user-attachments/assets/1bb08fbd-f7ae-48de-81fd-5d81717404cf)

This user tried to loggin on 4 am, i think it is unusoal login. After submit it, it is true. So the answer is
```
2024-02-19 04:00:14
```

### Question 4
What is the Fingerprint of the attacker's public key <br>
We can get from the picture on question 3, copy the SHA256. The answer is
```
OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4
```
### Question 5
What is the first command the attacker executed after logging in <br>
Check in the bash_history.txt after this time `2024-02-19 04:00:14`. The answer is
```
whoami
```

### Question 6
What is the final command the attacker executed before logging out <br>
Check in the bash_history.txt before this time `2024-02-19 04:38:17` (logout time). The answer is
```
./setup
```

## Flag
```
Here is the flag: HTB{4n_unusual_s1ght1ng_1n_SSH_l0gs!}                                                                                                       
```
