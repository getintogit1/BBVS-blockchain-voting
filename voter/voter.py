#!/usr/bin/env python3
from utils.commutativeEncryptionLogic import chunkstring, generateKeys, crypt
from utils.writeLogs import writeLog


class Voter:
    def __init__(self, name, wallet, choice):
        self.name = name
        self._wallet = wallet
        self.__choice = choice
        self._e = None
        self._d = None
        self.__key_pair = None
        self._initial_wallet_address = None
        self._encrypted_wallet_address= None


    @property
    def initial_wallet_address(self):
        return self._initial_wallet_address
    
    @initial_wallet_address.setter 
    def initial_wallet_address(self, value):
        self._initial_wallet_address = value

    @property
    def e(self):
        return self._e

    @property
    def d(self):
        return self._d

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter 
    def wallet(self, value):
        self._wallet = value 


    def generateKeyPair(self, PRIME):
        e, d = generateKeys(PRIME)
        self._e = e
        self._d = d
        self._key_pair = e, d
        return e, d

    def paddingHash(self, FRAGMENT_SIZE):
        return self._wallet.address + " " * (
            (FRAGMENT_SIZE - (len(self._wallet.address) % FRAGMENT_SIZE)) % FRAGMENT_SIZE
        )

    def full_decrypt_one_hash(self, partial_hash, FRAGMENT_SIZE, PRIME):
        """
        Entschlüsselt mit dem eigenen privaten Schlüssel genau einmal.
        (Nutze für Verifikation.)
        """
        print("Voter name: ", self.name)
        print("Recovered Verschlüsselt: ", partial_hash)
        print("Stored Verschlüsselt:", self._encrypted_wallet_address)
        padded_partial = partial_hash + " " * (
            (FRAGMENT_SIZE - (len(partial_hash) % FRAGMENT_SIZE)) % FRAGMENT_SIZE
        )
        fragments = chunkstring(padded_partial, FRAGMENT_SIZE)
        decrypted_chunks = []
        for frag in fragments:
            decrypted_chunk = crypt(frag, self._d, PRIME)
            decrypted_chunks.append(decrypted_chunk)
            # Combine and strip padding
        decrypted_msg = "".join(decrypted_chunks).strip()
        return decrypted_msg

    def encrypt_one_hash_with_my_key(self, original_hash, FRAGMENT_SIZE, PRIME):
        """
        Verschlüsselt einen Klartext-Hash einmalig mit dem eigenen öffentlichen Schlüssel.
        (Nutze für Verifikation.)
        """
        print("Voter name: ", self.name)
        print(
            "Ein Zufälliger Hash aus dem anfnags pool -> nicht zurückschißbar auf idnetität: ",
            original_hash,
        )
        print("Stored Oriinal: ", self._initial_wallet_address)
        padded_msg = original_hash + " " * (
            (FRAGMENT_SIZE - (len(original_hash) % FRAGMENT_SIZE)) % FRAGMENT_SIZE
        )
        fragments = chunkstring(padded_msg, FRAGMENT_SIZE)  # Split into fragments
        encrypted_chunks = []  # Encrypt each fragment using your private key
        for frag in fragments:
            encrypted_chunk = crypt(frag, self._e, PRIME)
            encrypted_chunks.append(encrypted_chunk)
        encrypted_msg = "".join(encrypted_chunks)
        return encrypted_msg

    def verify_my_vote(self, FRAGMENT_SIZE, PRIME, log_path):
        """
        1) Entschlüssle mixed_hash einmal mit d
        2) Verschlüssele das Ergebnis wieder mit e
        3) Schreib die Werte ins Log
        """
        one_time_encrypted_address = self._wallet.address
        hash_belonging_to_anybody = self.full_decrypt_one_hash(
            one_time_encrypted_address, FRAGMENT_SIZE, PRIME
        )

        reencr = self.encrypt_one_hash_with_my_key(
            hash_belonging_to_anybody, FRAGMENT_SIZE, PRIME
        )

        writeLog(
            log_path,
            self.name,
            one_time_encrypted_address,
            hash_belonging_to_anybody,
            reencr,
            self._initial_wallet_address
        )

    def __repr__(self):
        return f"Name: {self.name} \nWallet: {self._wallet.address} \nKeys: {self.__key_pair} \nPreffered Candidate: {self.__choice} \n\n "
