#!/usr/bin/env python3

from Crypto.Util.number     import getPrime
from Crypto.Random          import get_random_bytes
from blockchain.wallet      import InitialWallet, Wallet
from blockchain.blockchain  import Blockchain
from utils.votingFunctions  import makeAndCountVotes, makeInitialTransactions 
from utils.writeLogs        import storeBlockChain
from utils.utils            import getUserInput, createFakeNames
from voter.voter            import Voter
from utils.encryptionDecryptionFunctions import encryptAndDecrypt  
import random



def main():
    # Size of Voting Proces
    VOTES_PER_BLOCK, NUMBER_OF_VOTERS, MYID = getUserInput()
    NUM_OF_BLOCKS = NUMBER_OF_VOTERS // VOTES_PER_BLOCK

    # Blockchain Setup
    blockchain = Blockchain()
    initial_wallet = InitialWallet(NUMBER_OF_VOTERS)
    wallets = [Wallet() for _ in range(NUMBER_OF_VOTERS)]

    makeInitialTransactions(initial_wallet, wallets, blockchain)
    storeBlockChain(blockchain)

    # Params for Commutative Encryption
    primebits = 64
    PRIME = getPrime(primebits, randfunc=get_random_bytes)
    FRAGMENT_SIZE = primebits // 8                                              
    participant_names = createFakeNames(NUMBER_OF_VOTERS)

    # Voters Setup
    voters = []
    for name, wallet in zip(participant_names, wallets):
        choice = random.choices(["A","B"])
        voter = Voter(name, wallet, choice)
        voter.generateKeyPair(PRIME)
        voter.initial_wallet_address = voter.wallet.address
        voters.append(voter)

    encryptAndDecrypt(voters, FRAGMENT_SIZE, PRIME) 
    
    voter = voters[MYID]
    voter.verify_my_vote( FRAGMENT_SIZE, PRIME, "data/verifyMyVote.json")
    
    random.shuffle(voters) # voter wählen in der regel zufällig und nithct 1:1 in der Reihenfolge in der sie ihre wahlunterlagen erhalten haben
    votesA, votesB = makeAndCountVotes(voters, blockchain, NUM_OF_BLOCKS, VOTES_PER_BLOCK)
    storeBlockChain(blockchain)
    print("Votes A: ", votesA) 
    print("Votes B: ", votesB)
    

if __name__ == "__main__":
    main()
