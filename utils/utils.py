#!/usr/bin/env python3

from faker import Faker


def compare(walletHashes, VoterWalletHashes): 
    for orig, compared  in zip(walletHashes, VoterWalletHashes):
        print(f"Original: {orig}")
        print(f"Compared : {compared}")
        print("MATCH?  :", "YES" if orig == compared else "NO")
        print("-" * 75)
    return walletHashes == VoterWalletHashes


def createFakeNames(NUMBER_OF_VOTERS):
    fake = Faker()
    if NUMBER_OF_VOTERS == 3:
        return ["Rivest", "Shamir", "Adleman"]
    participant_names = [fake.name() for _ in range(NUMBER_OF_VOTERS)]
    return participant_names


def getUserInput():
    while True:
        VOTES_PER_BLOCK = int(input("Enter number of votes per block: "))
        NUMBER_OF_VOTERS = int(input("Enter number of voters: "))
        MYID = int(input("Enter number of your ID: "))
        if NUMBER_OF_VOTERS % VOTES_PER_BLOCK == 0 and MYID < NUMBER_OF_VOTERS :
            break
        else:
            print("Number of voters must be divisible by votes per block. Try again.")
            print("Your ID needs to be smaller than total amount of voters. Try again.")
    return VOTES_PER_BLOCK, NUMBER_OF_VOTERS, MYID
