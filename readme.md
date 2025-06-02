# Blockchain-Based Voting System Simulation

A Python-based simulation of a secure, anonymous, and verifiable voting system using **commutative asymmetric encryption** and a **blockchain-like ledger**. This system enables voters to **cast anonymized votes**, **verify their own votes**, and **tally the results** in a transparent yet private way.

> 🔐 Inspired by the **SRA Mental Poker** protocol and the **Massey-Omura Cryptosystem**.

---

## Features

- **Anonymous Voting** – Cast encrypted votes while preserving voter privacy.
- **Commutative Asymmetric Encryption** – Enables encryption/decryption in any order without compromising results.
- **Vote Verification** – Each voter can verify that their vote is included in the ledger.
- **Secure Vote Counting** – Votes are decrypted and tallied securely.
- **Blockchain Simulation** – Each vote is a block in a linked chain to ensure transparency and immutability.

---
## Massey Omura Cryptosystem
Ref:
- [Buchanan, William J (2025)](https://asecuritysite.com/commul/massey2)
![image](https://github.com/user-attachments/assets/092e709e-648f-4b46-802b-4e75b5166699)


---
## Mental Poker Protocol
The Mental Poker protocol by Shamir, Rivest, and Adleman (SRA) allows two or more players to "play" a fair card game without trusting each other, using commutative encryption. In the context of voting, we use this approach to shuffle, encrypt, and anonymously process ballots.

Privacy: No single party knows the full vote before collaborative decryption

Fairness: All parties apply and remove encryption without learning the vote

Commutativity: Order of encryption and decryption doesn't affect correctness

Why Use This in Voting?
This protocol ensures that:

Voters don't trust a central authority

Ballots are shuffled and anonymized

Anyone can verify that their vote was included and not altered

Combined with Massey–Omura
When combined with the Massey–Omura cryptosystem, this approach forms the backbone of secure, anonymous, verifiable voting simulations—like the one implemented in this project.

---

## References

Python <br>
Cryptographic principles from:
  - [Mental Poker (SRA Protocol)](https://en.wikipedia.org/wiki/Mental_poker)
  - [Massey-Omura](https://asecuritysite.com/commul/massey2)

---

## 📦 Installation & Usage

    # 1. Clone the repository
    git clone https://github.com/getintogit1/BBVS-Simulation.git
    cd BBVS-Simulation

    # 2. Install Dependencies
    pip install -r requirements.txt

    # 3. Run main.py
    python main.py 

---

## Example
The following screenshot shows a simulation run with 240 voters and 2 candidates (A and B). The blockchain records each vote as a transaction, grouped into mined blocks with unique hashes.


🔍 What's Visible:

Each mined block displays:

Block ID

Hash and Previous Hash

Nonce used for proof-of-work

Timestamp, Version, and Difficulty Bits

A list of encrypted transactions (votes)
The Target value (mining difficulty) gets dynamically adjusted similiar to Bitcoin.

🔄 Encrypted Transactions:

Each vote is stored as a transaction in the blockchain using commutative encryption

Transaction entries reflect anonymized sender/receiver values

🧮 Final Vote Count:

Candidate A received: 129 votes

Candidate B received: 111 votes

Notes:
Even though transactions look obfuscated, voters can verify their individual votes through the encryption chain.

This demonstrates a fully simulated, decentralized, and verifiable voting process using the Massey–Omura encryption technique and mental poker principles.


![Output for 240 voters and two Candidates](image.png)



