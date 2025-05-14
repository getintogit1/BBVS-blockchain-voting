#!/usr/bin/env python3

import json


def writeLog(log_file_path, owner, w_hash_others_can_see, original_hash, one_key_encrypted_hash):
    log_entry = {
    "Your Name": owner,
    "Your Hash other people can see": w_hash_others_can_see,
    "Original Wallet Hash (from init)": original_hash,
    "Recovered Original Hash (After Final Decryption)": original_hash,
    "Re-Encrypted Hash (Just with Your Key)": one_key_encrypted_hash,
    "To verify if your vote got couted look in Blockchain for": one_key_encrypted_hash
    }    

    with open(log_file_path, "w") as f:
        json.dump(log_entry, f, indent=4)
    print(f"\n Log saved to {log_file_path}")  


def storeBlockChain(blockchain):
    with open("data/blockchain.json", "w") as f:
        chain_data = [blockToDict(block) for block in blockchain.chain]
        json.dump(chain_data, f, indent=2)


def blockToDict(block):
    return {
        "bits": block.bits,
        "version": block.version,
        "hash": block.hash,
        "previous_hash": block.prev_block_hash,
        "nonce": block.nonce,
        "timestamp": block.time_stamp,
        "transactions": [tx.to_dict() for tx in block.transactions],
    }
