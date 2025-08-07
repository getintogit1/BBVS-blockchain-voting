#!/usr/bin/env python3

import libnum
import random
from typing import Generator


def chunkstring(string, length) -> Generator[str, None, None]:
    """Split a string into equal-length chunks using a generator."""
    return (string[0 + i : length + i] for i in range(0, len(string), length))


def generateKeys(prime):
    """
    Generate a random public/private key pair (e, d) for a given prime.
    Ensures that e is coprime to (prime - 1) and finds the modular inverse d.
    """
    while True:  # geeigntes e finden
        e = random.randint(3, prime - 2)  # zufällige ganzzahl wählen
        if (
            libnum.gcd(e, prime - 1) == 1
        ):  # e ist teilerfremd zu prime - 1 -> e hat ein multiplikatives inverse
            break
    d = libnum.invmod(
        e, prime - 1
    )  # d ist das multiplikative Inverse von e in Z / (prime - 1)
    return e, d  # e zum ver- und d zum ent-schlüsseln


"""
b ist multiplikativ inverse zu a wenn a x b = 1
x -> x^e 
(x^e)^d = x 
"""


def crypt(chunk, key, prime):
    """
    converts text chunks into numbers and enrcypt them with a large prime
    """
    num = 0
    for c in chunk:  # für jeden char im string
        num *= 256  # generiere pseudo byte representation
        num += ord(c)
    res = pow(num, key, prime)
    #print(num)
    vect = []
    for _ in range(len(chunk)):
        vect.append(chr(res % 256))
        res //= 256
    return "".join(
        reversed(vect)
    )  # es wird in umgekehrter reihenfolge mit d entschlüsselt


"""

!Num needs to be smaller than prime 

i want to encrypt - decrypt : Helloworld 
for every char in my string: 
    i am converting that char into a byte representation :
    num = ord(H) * 256⁹ + ord(e) * 256⁸ + ... + ord(d) * 256⁰
    thats a huge number 
    If the prime is a 64-bit number, this will fail because:
        num >= prime -> modular exponentiation wont decrypt correctly


i want to encrypt - decrypt : Helloworld but in chunks of len 3 
['Hel', 'low', 'orl', 'd']
for ever char in my chunk:
    i am converting that char into a byte representation :
    num = ord(chunk[0]) * 256² + ord(chunk[1]) * 256¹ + ord(chunk[2]) * 256⁰
    The resulting number is much smaller and fits into a 64-bit prime

"""


"""
Padding:
ede Operation erwartet, dass der Eingangswert  x eine Zahl < p ist. Ein SHA-256-Hash (oder was auch immer dein Wallet-Hash ist) kann aber viel länger sein als der Wertebereich
Padding füllt genau so viele Leerzeichen (oder Nullen) ans Ende an, dass der gepaddete String durchgängig in Chunks der Länge FRAGMENT_SIZE zerlegbar ist.

Nach dem Decrypt entfernst du (.strip()) die Padding-Zeichen wieder, und bekommst genau den ursprünglichen Hash zurück.

Chunking sorgt dafür, dass jeder Block numerisch klein genug ist für deine modulare Potenzierung.

Padding garantiert, dass jedes Stück immer genau FRAGMENT_SIZE lang ist, damit du später ohne Rest wieder sauber zusammenfügen kannst.
"""


def run_test():
    text = "Helloworld"
    prime = 2**64 - 59
    e, d = generateKeys(prime)

    print(f"Using prime: {prime}")
    print(f"Generated public key e: {e}\n")

    print("Chunk length: 10 (whole string)")
    encrpyted_chunks_10 = []
    for chunk in chunkstring(text, 10):
        encrpyted_chunks_10.append(crypt(chunk, e, prime))
    encrypted_msg_10 = "".join(encrpyted_chunks_10)

    print("\n Chunk length: 3")
    encrypted_chunks_3 = []
    for chunk in chunkstring(text, 3):
        encrypted_chunks_3.append(crypt(chunk, e, prime))
    encrypted_msg_3 = "".join(encrypted_chunks_3)
    print("Encrypted 10: ", encrypted_msg_10)
    print("Encrypted 3: ", encrypted_msg_3)

    decrypted_chunks_10 = [crypt(chunk, d, prime) for chunk in encrpyted_chunks_10]
    print("Decrypted 10: ", "".join(decrypted_chunks_10))
    decrypted_chunks_3 = [crypt(chunk, d, prime) for chunk in encrypted_chunks_3]
    print("Decrypted 3: ", "".join(decrypted_chunks_3))


if __name__ == "__main__":
    run_test()
