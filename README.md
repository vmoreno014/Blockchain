# Blockchain

## Table of Contents
1. [Asymmetric Cryptography](#asym-crypto)
2. [Cryptographic Hash Functions](#crypto-hash)
3. [SHA-256](#sha-256)
4. [Merkle Trees](#merkle-trees)
5. [Proof of Work](#proof-of-work)
6. [Blockchain](#blockchain)
7. Distributed Ledger
8. Digital Signatures
9. Bitcoin

## Asymmetric Cryptography <a name="asym-crypto"></a>
- *Symmetric cryptography* uses the same key for encryption and decryption.

<img src="images/symmetric-encryption.png" width="400" alt="symmetric encryption"/>  

[Image reference](https://www.101computing.net/symmetric-vs-asymmetric-encryption/)  

- *Asymmetric cryptography* uses two different keys for encryption and decryption.


<img src="images/asymmetric-encryption.png" width="400" alt="asymmetric encryption"/>  

[Image reference](https://www.101computing.net/symmetric-vs-asymmetric-encryption/) 

Asymmetric cryptography is a cryptographic system that uses **two different keys**: a public key and a private key.  

| Public Key | Private Key |
|------------|-------------|
| Can be shared with anyone | Should be kept secret |
| Encryption | Decryption  |
| Signing    | Verification |

### Resources
[Video by Simply Explained](https://youtu.be/AQDCe585Lnc)  
[Online key demo](https://andersbrownworth.com/blockchain/public-private-keys/keys)  
[Online RSA key generator](https://travistidwell.com/jsencrypt/demo/)

## Cryptographic Hash Functions <a name="crypto-hash"></a>
This are a special class of hash functions that have certain properties that make them suitable for cryptography.

### Characteristics of cryptographic hash functions:
- **Deterministic**: the same input always produces the same output.
- **One-way**: it is infeasible to compute the input data from its hash value.
- **Collision resistant**: it is infeasible to find two different inputs that produce the same hash value.
- **Computationally efficient**: it is easy to compute the hash value for any given input data.
- **Hide information**: the output looks random and does not reveal any information about the input data.

<img src="images/crypto-hash-functions.PNG" width="400" alt="asymmetric encryption"/>

### Resources
[Video by Lisk](https://youtu.be/2BldESGZKB8)  
[What is hashing?](https://www.educative.io/answers/what-is-hashing)  
[Video by Khan Academy](https://youtu.be/0WiTaBI82Mc)  
[Online SHA-256 hash demo](https://andersbrownworth.com/blockchain/hash)  
[Cryptographic vs Non-crpytographic](https://dadario.com.br/cryptographic-and-non-cryptographic-hash-functions/)  
[Video by 3Blue1Brown](https://youtu.be/bBC-nXj3Ng4?t=747)


## SHA-256 <a name="sha-256"></a>
SHA stands for Secure Hash Algorithm.  
SHA-256 is a cryptographic hash function that takes an input and produces a 256-bit (32-byte) hash value.  
This hash value is known as a [**message digest**](https://www.geeksforgeeks.org/message-digest-in-information-security/) (*very important*)   – typically rendered as a hexadecimal number, 64 digits (0-f) long.

### Resources
[SHA-256 online algorithm](https://sha256algorithm.com/)  
[Online SHA-256 generator](https://emn178.github.io/online-tools/sha256.html)  
[Steps in SHA-256](https://www.educative.io/answers/what-are-the-different-steps-in-sha-256)  
[Video by Xiuminseokie21](youtube.com/watch?v=9xs4eWOAG7Y)  


## Merkle Trees <a name="merkle-trees"></a>
A Merkle tree is a data structure that allows for efficient verification of the contents of large data structures.  
It is a tree in which every leaf node is labelled with the cryptographic hash of a data block and every non-leaf   
node is labelled with the cryptographic hash of the labels of its child nodes.

<img src="images/merkle-tree.png" width="400" alt="merkle tree"/>  

[Image reference](https://medium.com/coinmonks/merkle-trees-concepts-and-use-cases-5da873702318)

### Resources
[Intro to Merkle Trees](https://academy.binance.com/es/articles/merkle-trees-and-merkle-roots-explained)  
[Video by Cryptoeconomic Study](https://youtu.be/r_vrvoGd3RU)

## Proof of Work <a name="proof-of-work"></a>
Proof of work is a piece of data which is difficult (costly, time-consuming) to produce but easy for others to verify.  
This piece of data needs to comply a set of rules that are difficult to satisfy but easy to verify.

Bitcoin uses the proof of work algorithm to determine the order of transactions in the blockchain.
Etherium uses the proof of stake algorithm to determine the order of transactions in the blockchain.  

<img src="images/proof-of-work.jpg" width="600" alt="proof of work">  

[Image reference](https://forkast.news/proof-of-work-what-is-it-bitcoin-halving/)

### Resources
[Video by Binance Academy](https://youtu.be/3EUAcxhuoU4)  
[PoW by Investopedia](https://www.investopedia.com/terms/p/proof-work.asp)  
[Video by Khan Academy](https://youtu.be/9V1bipPkCTU)  
[PoW vs PoS](https://blockgeeks.com/guides/proof-of-work-vs-proof-of-stake/)  

## Blockchain <a name="blockchain"></a>
A blockchain is a distributed ledger that is used to record transactions across many computers so that the  
record cannot be altered retroactively without the alteration of all subsequent blocks and the collusion of the network.

Blockchain is a combination of all the concepts we have explained above.  


### Resources

[Video by 3Blue1Brown](https://youtu.be/bBC-nXj3Ng4)  
[Video by Simply Explained](https://youtu.be/SSo_EIwHSd4)

## Bitcoin <a name="bitcoin"></a>

### Resources
[Khan Academy Course](https://www.khanacademy.org/economics-finance-domain/core-finance/money-and-banking#bitcoin)
