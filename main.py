#!/usr/bin/env python3

from Crypto.Util.number     import getPrime
from Crypto.Random          import get_random_bytes
from blockchain.wallet      import InitialWallet, Wallet
from blockchain.blockchain  import Blockchain
from utils.votingFunctions  import makeAndCountVotes, makeInitialTransactions 
from utils.writeLogs        import writeLog, storeBlockChain
from utils.utils            import getUserInput, createFakeNames
from utils.encryptionDecryptionFunctions import(
    generateKeyPair,
    encryptAndDecrypt,  
    fullyDecryptOneHash,
    encryptWalletHashWithKey
)
import random



def main():
    # Size of Voting Proces
    VOTES_PER_BLOCK, NUMBER_OF_VOTERS, MYID = getUserInput()
    NUM_OF_BLOCKS = NUMBER_OF_VOTERS // VOTES_PER_BLOCK

    # Blockchain Setup
    blockchain = Blockchain()
    wallets = [Wallet() for _ in range(NUMBER_OF_VOTERS)]
    random.shuffle(wallets)
    wallet_hashes = [w.hash for w in wallets]
    random.shuffle(wallet_hashes)
    initial_wallet= InitialWallet(NUMBER_OF_VOTERS)
    makeInitialTransactions(initial_wallet, wallets, blockchain)

    # Params for Commutative Encryption
    primebits = 64
    PRIME = getPrime(primebits, randfunc=get_random_bytes)
    FRAGMENT_SIZE = primebits // 8
    participant_names = createFakeNames(NUMBER_OF_VOTERS)
    keys = generateKeyPair(PRIME, participant_names)

    wHashes_owner_key_remaining = encryptAndDecrypt(wallet_hashes, FRAGMENT_SIZE, PRIME, keys, participant_names, wallets) 
    votesA, votesB = makeAndCountVotes(wallets, blockchain, NUM_OF_BLOCKS, VOTES_PER_BLOCK)
    storeBlockChain(blockchain)
    print("Votes A: ", votesA) 
    print("Votes B: ", votesB)
     
    # Simulating A Voter That Knows His Private key Can see His Vote in the log created + lock up in blockchain
    w_hash_others_can_see = wHashes_owner_key_remaining[MYID]
    owner = participant_names[MYID]
    my_key_decryption = keys[owner]["d"]
    original_hash = fullyDecryptOneHash(w_hash_others_can_see   , my_key_decryption, FRAGMENT_SIZE, PRIME)
    my_key_encryption = keys[participant_names[MYID]]["e"]
    one_key_encrypted_hash =  encryptWalletHashWithKey(original_hash, my_key_encryption, FRAGMENT_SIZE, PRIME)
    log_file_path = "data/verifyMyVote.json"
    writeLog(log_file_path, owner, w_hash_others_can_see, original_hash, one_key_encrypted_hash)
  

if __name__ == "__main__":
    main()
