#!/usr/bin/env python3

from utils.commutativeEncryptionLogic import chunkstring, generateKeys, crypt


def generateKeyPair(PRIME, participant_names): 
    keys = {}
    for name in participant_names:
        e, d = generateKeys(PRIME)
        keys[name] = {'e': e, 'd': d}
    return keys


def encryptAndDecrypt(walletHashes, FRAGMENT_SIZE, PRIME, keys, participant_names, wallets):
    VoterWalletHashes = []
    for i, msg in enumerate(walletHashes):
        padded_msg = msg + " " * ((FRAGMENT_SIZE - (len(msg) % FRAGMENT_SIZE)) % FRAGMENT_SIZE)
        fragments = chunkstring(padded_msg, FRAGMENT_SIZE)
        encrypted_msg = encrypt(fragments, keys, PRIME)
        owner = participant_names[i]  
        decryption_order = [name for name in participant_names if name != owner]
        decryt(VoterWalletHashes, encrypted_msg, FRAGMENT_SIZE, PRIME, decryption_order, keys)
    updateWalletHashes(wallets, VoterWalletHashes)
    return VoterWalletHashes


def encrypt(fragments, keys, PRIME):
        encrypted_chunks = []
        for frag in fragments:
            c = frag
            for name in keys:
                c = crypt(c, keys[name]['e'], PRIME)
            encrypted_chunks.append(c)
        encrypted_msg = "".join(encrypted_chunks)
        return encrypted_msg


def decryt(VoterWalletHashes, encrypted_msg, FRAGMENT_SIZE, PRIME, decryption_order, keys):        
    decrypted_chunks_partial = []
    for frag in chunkstring(encrypted_msg, FRAGMENT_SIZE):
        p = frag
        for name in decryption_order:
            p = crypt(p, keys[name]['d'], PRIME)
        decrypted_chunks_partial.append(p)
    partial_msg = "".join(decrypted_chunks_partial).strip()
    VoterWalletHashes.append(partial_msg)
    return partial_msg


def updateWalletHashes(wallets, VoterWalletHashes):       
    for w, h in zip(wallets, VoterWalletHashes):
            w.hash = h


# not Used in Main, its just to Verify Pseudo gernerated Hashes for All VoterWalletHashes
# in a Real scenario unuseable
def decryptLastKeyForAll(VoterWalletHashes, participant_names, keys,FRAGMENT_SIZE, PRIME):
    FinalWalletHashes = []
    for i, partial in enumerate(VoterWalletHashes):
        owner = participant_names[i]                                            
        final_key = keys[owner]['d']                                            

        padded_partial = partial + " " * ((FRAGMENT_SIZE - (len(partial) % FRAGMENT_SIZE)) % FRAGMENT_SIZE)
        fragments = chunkstring(padded_partial, FRAGMENT_SIZE)

        decrypted_chunks_final = []
        for frag in fragments:
            final = crypt(frag, final_key, PRIME)
            decrypted_chunks_final.append(final)

        full_msg = "".join(decrypted_chunks_final).strip()
        FinalWalletHashes.append(full_msg)
    return FinalWalletHashes


# used for write logs in main.py 
def fullyDecryptOneHash(partial_hash, private_key, FRAGMENT_SIZE, PRIME):
    padded_partial = partial_hash + " " * ((FRAGMENT_SIZE - (len(partial_hash) % FRAGMENT_SIZE)) % FRAGMENT_SIZE)
    fragments = chunkstring(padded_partial, FRAGMENT_SIZE)
    decrypted_chunks = []
    for frag in fragments:
        decrypted_chunk = crypt(frag, private_key, PRIME)
        decrypted_chunks.append(decrypted_chunk)
    # Combine and strip padding
    decrypted_msg = "".join(decrypted_chunks).strip()
    return decrypted_msg

# used also for write logs in main.py
def encryptWalletHashWithKey(original_hash, private_key, FRAGMENT_SIZE, PRIME):
    padded_msg = original_hash + " " * ((FRAGMENT_SIZE - (len(original_hash) % FRAGMENT_SIZE)) % FRAGMENT_SIZE)
    fragments = chunkstring(padded_msg, FRAGMENT_SIZE)                          # Split into fragments
    encrypted_chunks = []                                                       # Encrypt each fragment using your private key
    for frag in fragments:
        encrypted_chunk = crypt(frag, private_key, PRIME)
        encrypted_chunks.append(encrypted_chunk)
    encrypted_msg = "".join(encrypted_chunks)
    return encrypted_msg




