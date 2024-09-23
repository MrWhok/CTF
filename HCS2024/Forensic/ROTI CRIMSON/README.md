# Roti Crimson
## Description
King Crimson sangat suka roti, tapi dia menyembunyikannya entah dimana.

Author: DJumanto
## Approach
In this challange, it was given jpg file. To solve it, i used steghide tool. <br>
`steghide extract -sf ROTI_CRIMSON.jpg` <br>
It will asked passphrase, just click enter. The output will be saved in rotyrot.txt. <br>
`cat rotyrot.txt` <br>
The output will be like this <br>
![Screenshot_2024-09-23_23_14_28](https://github.com/user-attachments/assets/a79d21ae-6698-4a55-b277-afa5d025cf43)
As we can see, it have flag format but its encoded. Decode it using this website (https://cryptii.com/pipes/caesar-cipher) with shift 23
## Flag
`HCS{St3gh1d3_4nd_R0t13_1s_4_g00d_C0mb1nat10n}`
