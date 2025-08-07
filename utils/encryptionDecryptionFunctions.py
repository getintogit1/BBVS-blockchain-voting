#!/usr/bin/env python3

from utils.commutativeEncryptionLogic import chunkstring, generateKeys, crypt
import random


def encryptAndDecrypt(voters, FRAGMENT_SIZE, PRIME):
    # Padding + Chunking: nur einmal für alle Hashes 
    messages = [
        list(chunkstring(v.paddingHash(FRAGMENT_SIZE), FRAGMENT_SIZE))
        for v in voters
    ]
   
    for voter in voters:
        # Kollektive Verschlüsselung: jede Nachricht durch alle e-Schlüssel von jedem voter 
        encrypted_msgs = [
            encrypt(chunks, voters, PRIME)
            for chunks in messages
        ]
        
        random.shuffle(encrypted_msgs)    

    # Jeder Wähler bekommt eine zufällige hash und entschlüsselt sie
    VoterWalletHashes = []
    for i, encrypted_chunks in enumerate(encrypted_msgs):
        owner_voter = voters[i]
        decr_voters = [v for v in voters if v is not owner_voter]
        # decrypt erwartet jetzt eine List[str]:
        partial = decrypt(
            encrypted_chunks,
            FRAGMENT_SIZE,
            PRIME,
            decr_voters
        )
        VoterWalletHashes.append(partial)
       
    updateWalletHashes(voters, VoterWalletHashes)
    return VoterWalletHashes


def encrypt(fragments, voters, PRIME):
    encrypted_chunks = list(fragments)
    for voter in voters:
        encrypted_chunks = [crypt(frag, voter._e, PRIME) for frag in encrypted_chunks]
        #random.shuffle(encrypted_chunks)
    #print("CHUNKS", len(encrypted_chunks), encrypted_chunks)
    return encrypted_chunks


def decrypt(encrypted_chunks, FRAGMENT_SIZE, PRIME, decryption_voters):
    # Entschlüssel-Reihenfolge umdrehen!
    reversed_voters = list(reversed(decryption_voters))
    decrypted = []
    for frag in encrypted_chunks:
        p = frag
        for voter in reversed_voters:
            p = crypt(p, voter._d, PRIME)
        decrypted.append(p)
    # joine alle Chunks
    return "".join(decrypted).strip()


def updateWalletHashes(voters, VoterWalletHashes):
    for v, h in zip(voters, VoterWalletHashes):
        v._wallet.address= h


