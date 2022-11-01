# Blockchain
with ⏳ and ❤ by [Victor Moreno Arribas](https://www.linkedin.com/in/vmorenoa) for learning purposes from the 
subject [Sistemas de Gestión de Seguridad de Sistemas de Información](https://www.ehu.eus/es/web/guest/grado-ingenieria-informatica/creditos-y-asignaturas?p_redirect=consultaAsignatura&p_cod_proceso=egr&p_anyo_acad=20220&p_ciclo=X&p_curso=4&p_cod_asignatura=26025) 
at the [Facultad de Informática](https://www.ehu.eus/es/web/guest/grado-ingenieria-informatica) in the campus of 
Gipuzkoa from the [Universidad del Pais Vasco](https://www.ehu.eus/en/web/guest/home) (UPV/EHU).

## Table of Contents
1. [Asymmetric Cryptography](#asymmetric-cryptography)
2. [SHA-256](#sha-256)
3. [Digital Signatures](#digital-signatures)
4. [Cryptographic Hash Functions](#crypto-hash)
5. [Merkle Trees](#merkle-trees)
6. [Proof of Work](#proof-of-work)
7. [Ledger](#ledger)
8. [Blockchain](#blockchain)
9. [Bitcoin](#bitcoin)

## [Blockchain example in Python](#example)


## 1. Asymmetric Cryptography <a name="asymmetric-cryptography"></a>
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

## 2. SHA-256 <a name="sha-256"></a>
SHA stands for Secure Hash Algorithm.  
SHA-256 is a cryptographic hash function that takes an input and produces a 256-bit (32-byte) hash value.  
This hash value is known as a [**message digest**](https://www.geeksforgeeks.org/message-digest-in-information-security/) (*very important*)   – typically rendered as a hexadecimal number, 64 digits (0-f) long.

<img src="images/sha-256.png" width="400" alt="sha-256"/>

[Image reference](https://www.freecodecamp.org/news/md5-vs-sha-1-vs-sha-2-which-is-the-most-secure-encryption-hash-and-how-to-check-them/)

### Resources
[SHA-256 online algorithm](https://sha256algorithm.com/)  
[Online SHA-256 generator](https://emn178.github.io/online-tools/sha256.html)  
[Steps in SHA-256](https://www.educative.io/answers/what-are-the-different-steps-in-sha-256)  
[Video by Xiuminseokie21](youtube.com/watch?v=9xs4eWOAG7Y)

## 3. Digital Signatures <a name="digital-signatures"></a>
A digital signature is a mathematical scheme for verifying the authenticity of a digital message or document.


#### Signing
**Input**: message, private key  
**Output**: signature

#### Verification
**Input**: message, signature, public key  
**Output**: true/false

<img src="images/digital-signatures.jpg" width="600" alt="digital signatures">

[Image reference](https://medium.com/@rohanassurvase/a-guide-to-understanding-digital-signatures-what-is-it-and-how-it-works-5f50e5962168)

### Characteristics of a good digital signature
- **Authentication**: Digital signature makes the receiver believe that the data was created and sent by the claimed user.
- **Non-Repudiation**: The sender cannot deny sending a message later on.
- **Integrity**: This ensures that the message was not altered during the transfer.
### Resources
[Video by khan Academy](https://youtu.be/Aq3a-_O2NcI)  
[Video by Lisk](https://youtu.be/JR4_RBb8A9Q)  
[Video by Computerphile](https://youtu.be/s22eJ1eVLTU)  
[Medium article](https://medium.com/@rohanassurvase/a-guide-to-understanding-digital-signatures-what-is-it-and-how-it-works-5f50e5962168)  
[Book for dummies](https://www.cryptomathic.com/hubfs/Documents/E-Books/Digital_Signatures_for_Dummies.pdf)  


## 4. Cryptographic Hash Functions <a name="crypto-hash"></a>
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

## 5. Merkle Trees <a name="merkle-trees"></a>
A Merkle tree is a data structure that allows for efficient verification of the contents of large data structures.  
It is a tree in which every leaf node is labelled with the cryptographic hash of a data block and every non-leaf   
node is labelled with the cryptographic hash of the labels of its child nodes.

<img src="images/merkle-tree.png" width="400" alt="merkle tree"/>  

[Image reference](https://medium.com/coinmonks/merkle-trees-concepts-and-use-cases-5da873702318)

### Resources
[Intro to Merkle Trees](https://academy.binance.com/es/articles/merkle-trees-and-merkle-roots-explained)  
[Video by Cryptoeconomic Study](https://youtu.be/r_vrvoGd3RU)

## 6. Proof of Work <a name="proof-of-work"></a>
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

## 7. Ledger <a name="ledger"></a>
A ledger is a record of transactions.
This is the key element to keep the integrity of the blockchain.

<img src="images/ledger.jpg" width="400" alt="ledger"/>

[Image reference](https://www.bbc.com/news/technology-32781244)

The ledger is distributed all over the network and it is updated by the nodes.  
If one node changes the ledger, in the following step it will be verified and just with a single bit been modified 
the hash will be completely different and the block will be rejected.  
The rest of the nodes still have an updated ledger that is valid.

### Resources
[Online demo ledger](https://andersbrownworth.com/blockchain/distributed)  
[Video by Sonar Systems](https://youtu.be/OBSBu3afgeE)  
[Video by Genesis Block HK](https://youtu.be/4b0A5XU3-tY)  
[Video by Anders Brownworth](https://youtu.be/_160oMzblY8)

## 8. Blockchain <a name="blockchain"></a>
A blockchain is a distributed ledger that is used to record transactions across many computers so that the  
record cannot be altered retroactively without the alteration of all subsequent blocks and the collusion of the network.

Blockchain is a combination of all the concepts we have explained above.  

<img src="images/blockchain-chain.png" width="400" alt="blockchain">

[Image reference](https://www.velotio.com/engineering-blog/introduction-to-blockchain-and-how-bitcoin-works)

### Resources
[Video by 3Blue1Brown](https://youtu.be/bBC-nXj3Ng4)  
[Video by Anders Brownworth](https://youtu.be/xIDL_akeras)  
[Video by Simply Explained](https://youtu.be/SSo_EIwHSd4)

## 9. Bitcoin <a name="bitcoin"></a>
Bitcoin is the first cryptocurrency and the most popular one.

<img src="images/evolution-bitcoin-size.png" width="600" alt="evolution of bitcoin size from 2009 to 2022">

[Image reference](https://www.statista.com/statistics/647523/worldwide-bitcoin-blockchain-size/)


### Resources
[Khan Academy Course](https://www.khanacademy.org/economics-finance-domain/core-finance/money-and-banking#bitcoin)

# Blockchain examples <a name="example"></a>
### Signer and hasher
First of all, we need to sign the files and also get the hash of a given file.
```python
import hashlib

# Generates the hash for a given filename
def hasher(file):
    with open(file, "rb") as f:
        bytes = f.read()  # read entire file as bytes
    return hashlib.sha256(bytes).hexdigest()
```

```python
import secrets

# Sign the file with an 8-len HEX string and a signature
def signer(file, signature):
    f = open(file, "a")
    sign = secrets.token_hex(4) + " " + signature
    f.write(sign + "\n")
    f.close()
    return sign
```

```python
import shutil
import os
import basics

# Signs a file with a given signature, and return the hash of the signed file
def block_hasher(path, signature):
    # makes a copy of the input file
    copy = shutil.copyfile(path, "signed.txt")

    # signs the file and return the last line added to the file
    sign = basics.signer(copy, signature)

    # hashes the file
    signed_hash = basics.hasher(copy)

    # copy the signed file to the input file
    shutil.copyfile(copy, path)

    # removes the copy
    os.remove(copy)
    return signed_hash
```

#### Example
```text
 --- CASE 1 --- 
Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

 --- CASE 2 --- 
Hash before signing: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
Hash after signing:  05b71e0acef1ec412c915ffad65bb3a7b38decba5bd7d8958685e1c9d32c6992

 --- CASE 3 --- 
Before signing: ['Hello World']
Hash: 8b41337cb9563e93cbc0c999d2c3f544eee93f2664b66ad58bcde3fcb5a5c54c
After signing:  ['Hello World\n', '40d654d2 G39']
```



With these test cases, we can observe some properties of the SHA-256 hash function as described in the [cruptographic hash functions section](#crypto-hash).  


**Hide information** and **non-predictable output**  
In the first case we can see that the hash value seems random, but it is not. 

**Collision resistant**  
With a 64 character hash (256 bits), it is very unlikely to find two different files with the same hash value.

**Deterministic** and **one-way**  
In the second case we can check that the SHA-256 hash function is deterministic, since the hash value of the file (*test.txt*) is the same as in the first case since we didn't change the file.  
Also, we can see that the hash function is one-way, since we can't get the original file from the hash value information.

**Computationaly efficient**  
After running the three test cases we can observe that the hash function is computationaly efficient, since it takes a lot less than 1 second to obtain the hash value.

### Zeros methods
As we have seen in the [proof of work section](#proof-of-work), the proof of work algorithm is based on finding a number that when hashed with the data of the block, the resulting hash starts with a given number of zeros.  
Therefore, we are going to implement some methods to find hashes with a given number of zeros.

```python
import os
import shutil
import blocks
import basics

# Finds a hash with a given number of zeros
def num_finder(file, signature, n_zeros):
    # if n_zeros = 2 then zeros = "00"
    zeros = __convert_string(n_zeros)

    # make a copy of input file
    copy = shutil.copyfile(file, "nf_tmp.txt")

    while True:
        # sign the copy and get it hash until it starts with at least n_zeros
        signed_hash = blocks.block_hasher(copy, signature)
        if signed_hash.startswith(zeros):
            return signed_hash
```

```python
# Number of zeros to string
def __convert_string(n):
    zeros = ""
    for i in range(n):
        zeros += "0"

    return zeros
```

When there are a lot of computers in the blockchain network that obtain a hash with a given number of zeros, the winner
that gets the transaction fee is the one that obtains the hash with the largest amount of zeros in less time.

```python
# Finds the maximum number of zeros under the given time
# We can't use num_find because process can take more time than the given seconds
def max_finder(path_input, path_output, signature, seconds):
    # counter of zeros that will be incremented each time a hash with n zeros is found
    max_zeros = 1

    # string of zeros
    zeros = __convert_string(max_zeros)

    # copy of the input file
    copy = shutil.copyfile(path_input, "mf_tmp.txt")

    # last valid hash obtained
    valid_hash = ""

    # time
    t = 0

    # timer starts now
    start = time.time()

    while t < seconds:
        # time left
        t = time.time() - start

        # hash of the copy
        signed_hash = blocks.block_hasher(copy, signature)

        if signed_hash.startswith(zeros):
            valid_hash = signed_hash

            # remove previous output file generated with fewer zeros
            if os.path.exists(path_output):
                os.remove(path_output)

            # copy is now the output file, is signed
            shutil.copyfile(copy, path_output)

            # increments the number of zeros, try to find a hash with more zeros
            max_zeros += 1
            zeros = __convert_string(max_zeros)

        # resets the file to remove the last signature
        os.remove(copy)
        copy = shutil.copyfile(path_input, "tmp.txt")

    os.remove(copy)
    return valid_hash
```

If we give more time to the max_finder method, we can find have more probability to find a hash with more zeros.

```text
 --- CASE 5 --- 
Search time: 20 seconds
Hash: 00079cef5307c6aef6fac056684699cc332cc4d22163aee2f242a6aacb0144e4
Last line of the output file: 308ece06 ikaslea
```

In this case, we found a hash with 3 zeros in 20 seconds. So, we were a little lucky, usually it would find a 
hash with 2 zeros in 20 seconds. And this is a proof of work.

In our case, we had to hash the file "SGSSI-22.CB.O2.txt" with signature "G39", into "SGSSI-22.CB.O2.VMOR.txt".

```python
def test_lab5():
    path_input = "SGSSI-22.CB.02.txt"
    path_output = "SGSSI-22.CB.02.VMOR.txt"
    signature = "G39"
    seconds = 20
    print("Search time: " + str(seconds) + " seconds")

    hash = max_finder(path_input, path_output, signature, seconds)
    print("Hash: " + hash)

    with open(path_output, "r") as f:
        print("Last line of the output file: " + f.readlines()[-1])
```

```text
 --- LAB 5 --- 
Search time: 20 seconds
Hash: 00e0dc3d6e03a8158da9a00cf00c10ca9667fa2a8ae246aab89a6a94d3039d43
Last line of the output file: f6cb905d G39
```

Now we are going to be the checkers instead of the miners, so we will have to check is a file is signed and if the 
hash of that file starts with zeros.

```python
import filecmp
import basics

def checker(path_input1, path_input2):
    # check if is the same file
    if path_input1 == path_input2:
        return False

    # check if the content is the same
    if not filecmp.cmp(path_input1, path_input2):
        with open(path_input1, "r") as f1:
            with open(path_input2, "r") as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()

                # checks every line except the last one
                for i in range(len(lines1) - 1):
                    if lines1[i] != lines2[i]:
                        return False

                # checks the last line
                if not re.match(r"[a-z0-9]{8} G([0-9]{2})+", lines2[-1]):
                    return False

    # check if the hash of the second file starts with zeros
    hash = basics.hasher(path_input2)
    if not hash.startswith("00"):
        return False

    return True
```

When we test with the files "SGSSI-22.CB.02.txt" and "SGSSI-22.CB.02.VMOR.txt", we get True.  
And that is correct, as the second file is the one we signed in the last test from LAB 5.
The hash of this file starts with 2 zeros and is signed by "G39".  

```text
Valid file:  True
```

As we are in a network with a lot of computers that are mining, we have to check a lot of files.
Therefore, now we are going to implement a method that checks a lot of files from the same folder and returns the winner.
We already mentioned, that the winner is the one that obtains the hash with the largest amount of zeros. 
In this case, all the files are in a folder, so we don't know the time that it took to each file to obtain the hash. 

```python
import os
import shutil

import basics
import checker

# Return the number of consecutive zeros at the beginning of the hash
def zeros_counter(hash):
    zeros = 0
    for char in hash:
        if char == "0":
            zeros += 1
        else:
            break
    return zeros

# Returns the last line of a file
def last_line(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return lines[-1]


def files_checker(path_input, directory):
    # dictionary with key=number of consecutive zeros and value=hash
    zeros_hash = {}
    hash_input = basics.hasher(path_input)
    zeros_input = zeros_counter(hash_input)
    line_input = last_line(path_input)
    zeros_hash[zeros_input] = (hash_input, line_input)

    # check every file in directory
    for file in os.listdir(directory):

        # path of the file
        path = os.path.join(directory, file)
        tmp1 = shutil.copyfile(path_input, "tmp1.txt")
        tmp2 = shutil.copyfile(path, "tmp2.txt")

        # check if the file is a valid candidate
        if checker.checker(tmp1, tmp2):
            hash = basics.hasher(tmp2)
            zeros = zeros_counter(hash)
            line = last_line(tmp2)
            zeros_hash[zeros] = (hash, line)

    # check if there is a tie in the max number of consecutive zeros
    max_zeros = max(zeros_hash.keys())
    winners = []
    for key in zeros_hash.keys():
        if key == max_zeros:
            winners.append(zeros_hash[key])

    # there is more than one winner
    if len(winners) > 1:
        winners.sort()
        return winners[0]

    # there is only one winner
    else:
        return winners[0]

tmp = files_checker("SGSSI-22.CB.02.VMOR.txt", "SGSSI-22.Lab06.CB.02.Candidatos")
print(tmp)
```

After analyzing all the files one by one, we create a dictionary that contains the hash of the file, the number of 
consecutive zeros as the key anf the last line (signature) to know who is the owner of the winner hash. 

```text
('00000068919edb1b9cc570cc592f754938680a7bdd82adb7e6517d0f5839e64b', '0bde8f37 G14')
```
