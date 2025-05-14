# 🗳️ Blockchain-Based Voting System Simulation

A Python-based simulation of a secure, anonymous, and verifiable voting system using **commutative asymmetric encryption** and a **blockchain-like ledger**. This system enables voters to **cast anonymized votes**, **verify their own votes**, and **tally the results** in a transparent yet private way.

> 🔐 Inspired by the **SRA Mental Poker** protocol and the **Massey-Omura Cryptosystem**.

---

## 🚀 Features

- ✅ **Anonymous Voting** – Cast encrypted votes while preserving voter privacy.
- 🔐 **Commutative Asymmetric Encryption** – Enables encryption/decryption in any order without compromising results.
- 🔎 **Vote Verification** – Each voter can verify that their vote is included in the ledger.
- 📊 **Secure Vote Counting** – Votes are decrypted and tallied securely.
- ⛓️ **Blockchain Simulation** – Each vote is a block in a linked chain to ensure transparency and immutability.

---
## Massey Omura Cryptosystem
This system uses exponentiation in the Galois Field 
𝐺
𝐹
(
2
𝑛
)
GF(2 
n
 ) for both encryption and decryption.

If we have a message 
𝑀
M, the encryption (where 
𝑝
p is a prime) is:

𝐶
=
𝐸
(
𝑒
,
𝑀
)
=
𝑀
𝑒
m
o
d
 
 
𝑝
C=E(e,M)=M 
e
 modp
Decryption is done using:

𝐷
(
𝑑
,
𝑀
)
=
𝐶
𝑑
m
o
d
 
 
𝑝
D(d,M)=C 
d
 modp
Where:

0
≤
𝑒
≤
2
𝑛
−
1
0≤e≤2 
n
 −1

gcd
⁡
(
𝑒
,
2
𝑛
−
1
)
=
1
gcd(e,2 
n
 −1)=1

The decryption exponent 
𝑑
d is defined as:

𝑑
𝑒
≡
1
m
o
d
 
 
(
2
𝑛
−
1
)
de≡1mod(2 
n
 −1)
Or equivalently:

𝑑
=
𝑒
−
1
m
o
d
 
 
(
2
𝑛
−
1
)
d=e 
−1
 mod(2 
n
 −1)
This works because the multiplicative group of the Galois field 
𝐺
𝐹
(
2
𝑛
)
GF(2 
n
 ) has order 
2
𝑛
−
1
2 
n
 −1, and Lagrange's theorem ensures:

𝑀
𝑑
𝑒
=
𝑀
M 
de
 =M
for all 
𝑀
∈
𝐺
𝐹
(
2
𝑛
)
M∈GF(2 
n
 ).

🌀 Commutative Encryption Property
One of the advantages of the Massey–Omura Cryptosystem is that it supports commutative encryption. This means that if:

Bob uses keys 
(
𝑒
𝑏
,
𝑑
𝑏
)
(e 
b
​
 ,d 
b
​
 )

Alice uses keys 
(
𝑒
𝑎
,
𝑑
𝑎
)
(e 
a
​
 ,d 
a
​
 )

Then the encryption operations can be applied in any order:

Cipher
=
𝐸
(
𝑒
𝑏
,
𝐸
(
𝑒
𝑎
,
𝑀
)
)
=
𝐸
(
𝑒
𝑎
,
𝐸
(
𝑒
𝑏
,
𝑀
)
)
Cipher=E(e 
b
​
 ,E(e 
a
​
 ,M))=E(e 
a
​
 ,E(e 
b
​
 ,M))
Decryption can also be reversed in any order:

𝐷
(
𝑑
𝑏
,
𝐷
(
𝑑
𝑎
,
Cipher
)
)
=
𝐷
(
𝑑
𝑎
,
𝐷
(
𝑑
𝑏
,
Cipher
)
)
D(d 
b
​
 ,D(d 
a
​
 ,Cipher))=D(d 
a
​
 ,D(d 
b
​
 ,Cipher))
This property enables anonymous and collaborative encryption/decryption, which is ideal for secure, verifiable voting systems.



---
## Mental Poker Protocol
The Mental Poker protocol by Shamir, Rivest, and Adleman (SRA) allows two or more players to "play" a fair card game without trusting each other, using commutative encryption. In the context of voting, we use this approach to shuffle, encrypt, and anonymously process ballots.

📌 Key Concepts
Every participant has their own commutative public-private key pair: 
(
𝑒
𝑖
,
𝑑
𝑖
)
(e 
i
​
 ,d 
i
​
 )

Messages (e.g., votes or cards) are encrypted multiple times, once per participant

Decryption occurs in reverse order of encryption, revealing the original message securely

🔁 Example Flow
Let the message (vote/card) be 
𝑀
M

Alice encrypts using her key 
𝑒
𝑎
e 
a
​
 :

𝐶
1
=
𝐸
(
𝑒
𝑎
,
𝑀
)
C 
1
​
 =E(e 
a
​
 ,M)
Bob further encrypts using his key 
𝑒
𝑏
e 
b
​
 :

𝐶
2
=
𝐸
(
𝑒
𝑏
,
𝐶
1
)
=
𝐸
(
𝑒
𝑏
,
𝐸
(
𝑒
𝑎
,
𝑀
)
)
C 
2
​
 =E(e 
b
​
 ,C 
1
​
 )=E(e 
b
​
 ,E(e 
a
​
 ,M))
Now Bob decrypts with 
𝑑
𝑏
d 
b
​
 :

𝐶
3
=
𝐷
(
𝑑
𝑏
,
𝐶
2
)
=
𝐷
(
𝑑
𝑏
,
𝐸
(
𝑒
𝑏
,
𝐸
(
𝑒
𝑎
,
𝑀
)
)
)
=
𝐸
(
𝑒
𝑎
,
𝑀
)
C 
3
​
 =D(d 
b
​
 ,C 
2
​
 )=D(d 
b
​
 ,E(e 
b
​
 ,E(e 
a
​
 ,M)))=E(e 
a
​
 ,M)
Finally, Alice decrypts with 
𝑑
𝑎
d 
a
​
 :

𝑀
=
𝐷
(
𝑑
𝑎
,
𝐶
3
)
=
𝐷
(
𝑑
𝑎
,
𝐸
(
𝑒
𝑎
,
𝑀
)
)
M=D(d 
a
​
 ,C 
3
​
 )=D(d 
a
​
 ,E(e 
a
​
 ,M))
✅ Properties
Privacy: No single party knows the full vote before collaborative decryption

Fairness: All parties apply and remove encryption without learning the vote

Commutativity: Order of encryption and decryption doesn't affect correctness

🗳️ Why Use This in Voting?
This protocol ensures that:

Voters don't trust a central authority

Ballots are shuffled and anonymized

Anyone can verify that their vote was included and not altered

🔐 Combined with Massey–Omura
When combined with the Massey–Omura cryptosystem, this approach forms the backbone of secure, anonymous, verifiable voting simulations—like the one implemented in this project.

📖 Further Reading
SRA Mental Poker Paper (1979)

Massey–Omura Cryptosystem

---

## 🛠️ Technologies Used

- 🐍 Python 
- 🔐 Custom commutative encryption algorithm
- 📚 Cryptographic principles from:
  - [Mental Poker (SRA Protocol)](https://en.wikipedia.org/wiki/Mental_poker)
  - [Massey-Omura](https://en.wikipedia.org/wiki/Massey-Omura-Schema)

---

## 📦 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/getintogit1/BBVS-Simulation.git
cd BBVS-Simulation

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Run main.py
python main.py ```

## Example
![Output for 240 voters and two Candidates](image.png)




## Example Output
