# Blockchain

## Table of Contents
1. [Asymmetric Cryptography](#asym-crypto)
2. [Cryptographic Hash Functions](#crypto-hash)
3. Merkle Trees
4. SHA-256
5. Proof of Work
6. Blockchain
7. Distributed Ledger

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
[Online SHA-256 hash demo](https://andersbrownworth.com/blockchain/hash)  
[Cryptographic vs Non-crpytographic](https://dadario.com.br/cryptographic-and-non-cryptographic-hash-functions/)







