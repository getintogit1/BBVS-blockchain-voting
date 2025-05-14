from utils.functionsForBlockEncryption import (
    hash256,
    intToLittleEndian,
    littleEndianToInt,
)

class BlockHeader:
    def __init__(self, version, prev_block_hash, time_stamp, bits):
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.time_stamp = time_stamp
        self.bits = bits
        self.nonce = 0
        self.hash = ""

    def mine(self, target):
        self.hash = target + 1

        while self.hash > target:
            self.hash = littleEndianToInt(
                hash256(
                    intToLittleEndian(self.version, 4)
                    + bytes.fromhex(self.prev_block_hash)[::-1]
                    + intToLittleEndian(self.time_stamp, 4)
                    + self.bits
                    + intToLittleEndian(self.nonce, 4)
                )
            )
            self.nonce += 1
            print(f"Mining Started {self.nonce}", end="\r")
        self.hash =  intToLittleEndian(self.hash, 32).hex()[::-1]
        self.bits = self.bits.hex()
