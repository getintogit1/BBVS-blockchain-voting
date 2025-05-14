#!/usr/bin/env python3

from Crypto.Hash import RIPEMD160
from hashlib import sha256
import hashlib


def hash256(s):
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def hash160(s):
    return RIPEMD160.new(sha256(s).digest()).digest()

def intToLittleEndian(n, length):
    return n.to_bytes(length, "little")


def littleEndianToInt(b):
    return int.from_bytes(b, "little")


def targetToBits(target: int) -> bytes:
    raw_bytes = target.to_bytes(32, "big")
    raw_bytes = raw_bytes.lstrip(b"\x00")                                       # <1>
    if raw_bytes[0] > 0x7F:                                                     # <2>
        exponent = len(raw_bytes) + 1
        coefficient = b"\x00" + raw_bytes[:2]
    else:
        exponent = len(raw_bytes)                                               # <3>
        coefficient = raw_bytes[:3]                                             # <4>
    new_bits = coefficient[::-1] + bytes([exponent])                            # <5>
    return new_bits




