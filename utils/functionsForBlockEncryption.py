#!/usr/bin/env python3

from Crypto.Hash import RIPEMD160
import hashlib


def hash256(s):
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def hash160(s):
    return RIPEMD160.new(hashlib.sha256(s).digest()).digest()


def intToLittleEndian(n, length):
    return n.to_bytes(length, "little")


def littleEndianToInt(b):
    return int.from_bytes(b, "little")


def targetToBits(target: int) -> bytes:
    raw_bytes = target.to_bytes(32, "big")
    raw_bytes = raw_bytes.lstrip(b"\x00")                                    
    if raw_bytes[0] > 0x7F:                                                   
        exponent = len(raw_bytes) + 1
        coefficient = b"\x00" + raw_bytes[:2]
    else:
        exponent = len(raw_bytes)                                              
        coefficient = raw_bytes[:3]                                             
    new_bits = coefficient[::-1] + bytes([exponent])                           
    raw_bytes = raw_bytes.lstrip(b"\x00")
    if raw_bytes[0] > 0x7F:
        exponent = len(raw_bytes) + 1
        coefficient = b"\x00" + raw_bytes[:2]
    else:
        exponent = len(raw_bytes)
        coefficient = raw_bytes[:3]
    new_bits = coefficient[::-1] + bytes([exponent])
    return new_bits
