#!/usr/bin/env python
import sys


def verify_flag(flag): pass
verify_flag.__code__ = verify_flag.__code__.__class__( 1 , 20 , 9 , 67 , 'y\x0c\x00|\x00\x00d\x01\x00\x17\x01Wn%\x00\x01\x01\x01x9\x00|\x00\x00D]\x10\x00}\x01\x00|\x01\x00|\x01\x007}\x01\x00q\x19\x00W~\x01\x00n\x1b\x00Xx\x17\x00t\x00\x00rJ\x00|\x00\x00|\x00\x007}\x00\x00q7\x00W~\x00\x00y\x08\x00t\x01\x00\x01Wn\x07\x00\x01\x01\x01n\x01\x00Xt\x02\x00|\x00\x00\x83\x01\x00d\x01\x00k\x02\x00sx\x00t\x03\x00r|\x00t\x03\x00S|\x00\x00j\x04\x00d\x02\x00\x83\x01\x00s\x8f\x00t\x03\x00S|\x00\x00j\x05\x00d\x03\x00\x83\x01\x00s\xb4\x00t\x03\x00S|\x00\x00j\x06\x00d\x02\x00\x83\x01\x00}\x00\x00na\x00t\x02\x00|\x00\x00\x83\x01\x00}\x02\x00|\x00\x00j\x07\x00d\x02\x00d\x04\x00\x83\x02\x00d\x05\x00\x19j\x08\x00d\x03\x00d\x04\x00\x83\x02\x00d\x01\x00\x19}\x00\x00y \x00t\x02\x00|\x00\x00\x83\x01\x00d\x06\x00\x17|\x02\x00k\x02\x00s\x05\x01t\t\x00\x82\x01\x00Wn\x08\x00\x01\x01\x01t\x03\x00SXd&\x00\x01|\x00\x00d\x08\x00j\x06\x00d\t\x00d\n\x00\x83\x02\x00k\x02\x00r1\x01t\x03\x00St\n\x00t\x0b\x00|\x00\x00\x83\x02\x00}\x00\x00t\x02\x00|\x00\x00\x83\x01\x00}\x02\x00|\x02\x00d\x0b\x00k\x03\x00r\\\x01t\x03\x00St\x0c\x00|\x00\x00\x83\x01\x00}\x03\x00|\x03\x00|\x02\x00\x16d\x0c\x00k\x03\x00r|\x01t\x03\x00S|\x03\x00|\x02\x00\x15}\x04\x00t\r\x00|\x04\x00\x83\x01\x00d\r\x00k\x03\x00r\x9c\x01t\x03\x00Sg\x00\x00|\x00\x00D]\x10\x00}\x05\x00|\x05\x00|\x04\x00A^\x02\x00q\xa3\x01}\x00\x00t\x0e\x00t\x0f\x00|\x00\x00\x83\x01\x00\x83\x01\x00}\x06\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x07\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x08\x00d\x01\x00g\x01\x00d\x07\x00\x14}\t\x00d\x01\x00g\x01\x00d\x07\x00\x14}\n\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x0b\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x0c\x00d\x01\x00g\x01\x00d\x07\x00\x14}\r\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x0e\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x0f\x00d\x01\x00g\x01\x00d\x07\x00\x14}\x10\x00xS\x02t\x10\x00t\x02\x00|\x07\x00\x83\x01\x00\x83\x01\x00D]?\x02}\x11\x00x\xc6\x01t\x10\x00t\x02\x00|\x08\x00\x83\x01\x00d\x04\x00\x18\x83\x01\x00D]\xae\x01}\x12\x00|\x07\x00|\x11\x00c\x02\x00\x19|\x00\x00|\x11\x00|\x12\x00\x17\x19N\x03<|\x08\x00|\x11\x00\x19|\x00\x00|\x11\x00|\x12\x00\x17\x19\x17d\x0e\x00k\x04\x00r\xbb\x02t\x03\x00S|\x08\x00|\x11\x00c\x02\x00\x19|\x00\x00|\x11\x00|\x12\x00\x17\x197\x03<|\t\x00|\x11\x00c\x02\x00\x19|\x00\x00|\x11\x00|\x12\x00\x14\x19N\x03<|\n\x00|\x11\x00\x19|\x00\x00|\x11\x00|\x12\x00\x14\x19\x17d\x0e\x00k\x04\x00r\x0b\x03t\x03\x00S|\n\x00|\x11\x00c\x02\x00\x19|\x00\x00|\x11\x00|\x12\x00\x14\x197\x03<|\x0b\x00|\x11\x00c\x02\x00\x19|\x00\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x19N\x03<|\x0c\x00|\x11\x00\x19|\x00\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x19\x17d\x0e\x00k\x04\x00rc\x03t\x03\x00S|\x0c\x00|\x11\x00c\x02\x00\x19|\x00\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x197\x03<|\r\x00|\x11\x00c\x02\x00\x19|\x06\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x19N\x03<|\x0e\x00|\x11\x00\x19|\x06\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x19\x17d\x0e\x00k\x04\x00r\xbf\x03t\x03\x00S|\x0e\x00|\x11\x00c\x02\x00\x19|\x06\x00d\x0f\x00|\x11\x00|\x12\x00\x14\x17\x197\x03<|\x0f\x00|\x11\x00c\x02\x00\x19|\x06\x00|\x11\x00|\x12\x00\x17\x19N\x03<|\x10\x00|\x11\x00\x19|\x06\x00|\x11\x00|\x12\x00\x17\x19\x17d\x0e\x00k\x04\x00r\x13\x04t\x03\x00S|\x10\x00|\x11\x00c\x02\x00\x19|\x06\x00|\x11\x00|\x12\x00\x17\x197\x03<q}\x02W|\x07\x00|\x11\x00c\x02\x00\x19d\x10\x007\x03<|\t\x00|\x11\x00c\x02\x00\x19d\x10\x007\x03<|\x0b\x00|\x11\x00c\x02\x00\x19d\x10\x007\x03<|\r\x00|\x11\x00c\x02\x00\x19d\x10\x007\x03<|\x0f\x00|\x11\x00c\x02\x00\x19d\x10\x007\x03<|\x0c\x00|\x11\x00c\x02\x00\x19d\x0f\x007\x03<|\x10\x00|\x11\x00c\x02\x00\x19d\x04\x007\x03<q`\x02WxJ\x00|\x07\x00|\t\x00|\x0b\x00|\r\x00|\x0f\x00|\n\x00|\x0c\x00|\x0e\x00|\x10\x00g\t\x00D]\'\x00}\x13\x00x\x1e\x00|\x13\x00D]\x16\x00}\x05\x00|\x05\x00d\x0e\x00k\x04\x00r\xd2\x04t\x03\x00Sq\xd2\x04Wq\xc5\x04Wd\x11\x00j\x11\x00t\n\x00t\r\x00|\x07\x00\x83\x02\x00\x83\x01\x00d\x12\x00k\x03\x00r\x12\x05t\x03\x00Sy&\x00d\x11\x00j\x11\x00t\n\x00t\r\x00|\x08\x00\x83\x02\x00\x83\x01\x00d\x13\x00k\x03\x00r7\x05t\x03\x00SWn\x12\x00\x04t\x12\x00k\n\x00rL\x05\x01\x01\x01t\x03\x00SXd\x11\x00j\x11\x00t\n\x00t\r\x00|\t\x00\x83\x02\x00\x83\x01\x00d\x14\x00k\x03\x00ro\x05t\x03\x00St\x13\x00|\n\x00\x83\x01\x00d\'\x00k\x03\x00r\x85\x05t\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\x0b\x00\x83\x02\x00\x83\x01\x00d\x1a\x00k\x03\x00r\xac\x05d\x1b\x00GHt\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\x0c\x00\x83\x02\x00\x83\x01\x00d\x1c\x00k\x03\x00r\xd3\x05d\x1d\x00GHt\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\r\x00\x83\x02\x00\x83\x01\x00d\x1e\x00k\x03\x00r\xfa\x05d\x1f\x00GHt\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\x0e\x00\x83\x02\x00\x83\x01\x00d \x00k\x03\x00r!\x06d!\x00GHt\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\x0f\x00\x83\x02\x00\x83\x01\x00d"\x00k\x03\x00rH\x06d#\x00GHt\x03\x00Sd\x11\x00j\x11\x00t\n\x00t\r\x00|\x10\x00\x83\x02\x00\x83\x01\x00d$\x00k\x03\x00ro\x06d%\x00GHt\x03\x00St\x00\x00S' , (None, 0, 'TMCTF{', '}', 1, -1, 7, 5, 'ReadEaring', 'adEa', 'dHer', 24, 9, 'h', 255, 8, 32, '', 'R) +6', 'l1:C(', ' RP%A', 236, 108, 102, 169, 93, ' L30Z', 'X2', ' j36~', 's2', ' M2S+', 'X3', '4e\x9c{E', 'S3', '6!2$D', 'X4', ']PaSs', 'S4', 10, (236, 108, 102, 169, 93)) , ('True', '\xe0\xa1\xb5\xe0\xa1\xb5HA', 'len', 'False', 'startswith', 'endswith', 'replace', 'split', 'rsplit', 'AssertionError', 'map', 'ord', 'sum', 'chr', 'list', 'reversed', 'xrange', 'join', 'ValueError', 'tuple') , ('inval', 'c', 'l', 's', 'sdl', 'x', 'ROFL', 'KYRYK', 'QQRTQ', 'KYRYJ', 'QQRTW', 'KYRYH', 'QQRTE', 'KYRYG', 'QQRTR', 'KYRYF', 'QQRTY', 'i', 'j', 'ary') , 'flag.py' , 'verify_flag' , 1337 , '\x00\x01\x03\x01\x0c\x01\x03\x01\r\x01\x0e\x02\x07\x02\t\x01\x0e\x02\x03\x02\x03\x01\x08\x01\x03\x01\x04\x02\x12\x01\x06\x01\x04\x01\x0f\x01\x04\x02\x0f\x01\x04\x01\x12\x03\x0c\x01&\x01\x03\x01 \x01\x03\x01\x05\x02\x04\x02\x18\x01\x04\x01\x0f\x01\x0c\x01\x0c\x01\x04\x01\x0c\x01\x10\x01\x04\x01\n\x01\x12\x01\x04\x01\x1d\x01\x12\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x01\r\x01\x19\x01\x1d\x01\x18\x01\x1c\x01\x04\x01\x18\x01\x18\x01\x1c\x01\x04\x01\x18\x01\x1c\x01 \x01\x04\x01\x1c\x01\x1c\x01 \x01\x04\x01\x1c\x01\x18\x01\x1c\x01\x04\x01\x1c\x01\x10\x01\x10\x01\x10\x01\x10\x01\x10\x01\x10\x01\x14\x01(\x01\r\x01\x0c\x01\x0c\x01\x1e\x01\x04\x01\x03\x01\x1e\x01\x08\x01\r\x01\x05\x07\x1e\x01\x04\x01\x12\x01\x04\x01\x1e\x01\x05\x01\x04\x01\x1e\x01\x05\x01\x04\x01\x1e\x01\x05\x01\x04\x01\x1e\x01\x05\x01\x04\x01\x1e\x01\x05\x01\x04\x01\x1e\x01\x05\x01\x04\x01' )


print verify_flag.__code__.co_consts
print verify_flag.__code__.co_varnames
print verify_flag.__code__.co_names
print len( verify_flag.__code__.co_code )

o = open( './bc_origin' , 'w+' )
o.write( verify_flag.__code__.co_code )
o.close()