
1. There is a initial Wallet that holds as many coins as there are allowed Voters
- in reality there would be a currency that is limited by the amout of allowed voters

2. there are [amount of voters] * wallets created and sended to the individual already registered voters
- each wallet contains keys to "log in"
- this projects dont aim to cover the authentifictaion step 
- could be my passport / videoident etc. 

3. The initial wallet sends excatly 1 coin to each wallet (transaction get shuffled and batched)

5. Now we have [amout of voters] * wallets with 1 coin in random order

6. Every wallet encrypts every other wallet

7. shuffle them 

8. Every wallet is encrpyted by * [amount of voters]

9. Every wallet gets decrypted until only owner key remains

10. Votes are casted, in the blockchain only the wallet with one key left on it are seen

11. A user can lookup his encrypted wallet in the blokchain and verify he has voted 

