STEP:

1. ```cmd
   gcc -nostdlib -static shellcode.s -o shellcode-elf
   ```
2. ```cmd
   objcopy --dump-section .text=shellcode-raw shellcode-elf
   ```
3. ```cmd
   (cat /home/hacker/shellcode-injection/lv2/shellcode-raw;cat) | ./babyshell_level2
   ```
