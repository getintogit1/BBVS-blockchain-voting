#!/usr/bin/env python3

import libnum
import random


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def generateKeys(prime):
    while True:
        e = random.randint(3, prime - 2)
        if libnum.gcd(e, prime - 1) == 1:
            break
    d = libnum.invmod(e, prime - 1)
    return e, d


def crypt(chunk, key, prime):
    num = 0
    for c in chunk:
        num *= 256
        num += ord(c)
    res = pow(num, key, prime)
    vect = []
    for _ in range(len(chunk)):
        vect.append(chr(res % 256))
        res //= 256
    return "".join(reversed(vect))
