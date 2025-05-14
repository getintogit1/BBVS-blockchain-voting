#!/usr/bin/env python3

from .block import Block
from utils.functionsForBlockEncryption import targetToBits
from .blockheader import BlockHeader
from time import time


ZERO_HASH = "0" * 64
VERSION = 1
INITIAL_TARGET = 0x0000FFFF00000000000000000000000000000000000000000000000000000000
DIFFICULTY_ADJUSTMENT_INTERVAL = 10
VERSION_INCREMENT_INTERVAL = 10

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.current_target = INITIAL_TARGET
        self.bits = targetToBits(INITIAL_TARGET)


    def createGenesisBlock(self):
        return Block([], ZERO_HASH)


    def addBlock(self, new_block):
        new_block.prev_block_hash = self.getLatestBlock().hash
        new_block.time_stamp = int(time())
        block_version = VERSION + len(self.chain) // VERSION_INCREMENT_INTERVAL
        block_header = BlockHeader(
            block_version,
            new_block.prev_block_hash, 
            new_block.time_stamp, 
            self.bits)
        block_header.mine(self.current_target)
        new_block.nonce = block_header.nonce
        new_block.hash = block_header.hash
        new_block.version = block_version
        new_block.bits = block_header.bits
        self.chain.append(new_block)
        print(f"Block {new_block} of {new_block.version} version mined successfully with Nonce value of {block_header.nonce}")     
        if len(self.chain) % DIFFICULTY_ADJUSTMENT_INTERVAL == 0:
            self.adjustDifficulty()


    def adjustDifficulty(self):
        new_target = self.current_target >> 1  
        self.current_target = new_target
        self.bits = targetToBits(self.current_target)
        print(f"Difficulty adjusted. New target: {hex(self.current_target)}")
    

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculateHash():
                return False
            if current.prev_block_hash != previous.hash:
                return False
        return True


    def getLatestBlock(self):
        return self.chain[-1] 
