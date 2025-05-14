#!/usr/bin/env python3

from blockchain.transaction import Transaction
from blockchain.wallet import CandidateWallet, InitialWallet
from blockchain.block import Block
import random

def makeInitialTransactions(initial_wallet: InitialWallet, wallets: list, blockchain):
    initial_transactions = []
    for wallet in wallets:
        initial_wallet.sendToken(wallet)
        tx = Transaction(initial_wallet, wallet)
        initial_transactions.append(tx)
    initial_transactions_block = Block(initial_transactions)    
    blockchain.addBlock(initial_transactions_block)

    

def makeAndCountVotes(wallets: list, blockchain, NUM_OF_BLOCKS, VOTES_PER_BLOCK) -> tuple[int, int]:
    wallet_candidateA = CandidateWallet(MAX_ALLOWED_TOKENS = NUM_OF_BLOCKS * VOTES_PER_BLOCK)
    wallet_candidateB = CandidateWallet(MAX_ALLOWED_TOKENS = NUM_OF_BLOCKS * VOTES_PER_BLOCK)
    for i in range(NUM_OF_BLOCKS):
        start = i * VOTES_PER_BLOCK
        end = start + VOTES_PER_BLOCK
        voting_transactions = makeVotes(wallets[start:end], wallet_candidateA, wallet_candidateB)
        voting_block = Block(voting_transactions)
        blockchain.addBlock(voting_block)

    votesA, votesB = tallyVotes(blockchain, wallet_candidateA, wallet_candidateB)
    return votesA, votesB


def makeVotes(voters, candidateA, candidateB):
    voting_transactions = []
    for voter in voters:
        choice = random.choice([candidateA, candidateB])
        voter.sendToken(choice)
        tx = Transaction(voter, choice)
        voting_transactions.append(tx)
    return voting_transactions


def tallyVotes(blockchain, candidate_A_addr, candidate_B_addr):
    count_A = 0
    count_B = 0
    for block in blockchain.chain[1:]:
        for tx in block.transactions:
            if tx.receiver == candidate_A_addr.hash:
                count_A += 1
            elif tx.receiver == candidate_B_addr.hash:
                count_B += 1
    return count_A, count_B


