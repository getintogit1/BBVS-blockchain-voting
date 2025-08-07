#!/usr/bin/env python3

from utils.functionsForBlockEncryption import( 
        hash256, 
        intToLittleEndian, 
        littleEndianToInt) 
from time import time


class Block:
    def __init__(self, transactions,prev_block_hash=""):
        self.transactions = transactions
        self.prev_block_hash = prev_block_hash
        self.nonce = 0
        self.time_stamp = int(time())
        self.version = None
        self.bits = None
        self.hash = self.calculateHash()

       
    def calculateHash(self):   
        raw_data = (
            "".join(str(tx.__dict__) for tx in self.transactions)
            + self.prev_block_hash
            + str(self.nonce)
            + str(self.time_stamp)
            + str(self.version)
            + str(self.bits)
        )
        hash_bytes = hash256(raw_data.encode())  
        data = littleEndianToInt(hash_bytes)
        return intToLittleEndian(data, 32).hex()[::-1]


    def __repr__(self):
        return (
            f"Block(\n"
            f"  Hash: {self.hash},\n"
            f"  Transactions: {self.transactions},\n"
            f"  Previous Hash: {self.prev_block_hash},\n"
            f"  Nonce: {self.nonce},\n"
            f"  Timestamp: {self.time_stamp})\n"
            f"  Version: {self.version})\n"  
            f"  Bits: {self.bits})\n" 
                f")"
        )
