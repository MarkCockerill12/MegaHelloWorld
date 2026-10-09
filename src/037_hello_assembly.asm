section .data
    msg db "Hello World", 0xA
    len equ $ - msg
section .text
    global _start
_start:
    mov rax, 1          ; system call for write
    mov rdi, 1          ; file handle 1 is stdout
    mov rsi, msg        ; address of string to output
    mov rdx, len        ; number of bytes
    syscall             ; invoke operating system to do the write
    mov rax, 60        ; system call for exit
    xor rdi, rdi        ; exit code 0
    syscall             ; invoke operating system to exit
