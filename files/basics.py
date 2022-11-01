# Generates the hash for a given filename
import hashlib
import os
import secrets


def hasher(file):
    with open(file, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        return hashlib.sha256(bytes).hexdigest()


def signer(file, signature):
    f = open(file, "a")
    sign = "\n" + secrets.token_hex(4) + " " + signature
    f.write(sign)
    f.close()
    return sign

# CASE 1: Hash of a file
def test_case1():
    # 1. Create a file
    file = open("test.txt", "w")
    file.write("Hello World")
    file.close()

    # 2. Hash the file
    hash = hasher("test.txt")

    # 3. Print the hash
    print("Hash: " + hash)

    # 4. Remove the testing file
    os.remove("test.txt")


# CASE 2: Hash of a file with a signature
def test_case2():
    # 1. Create a file
    file = open("test.txt", "w")
    file.write("Hello World")
    file.close()

    # 2. Hash the file before signing
    hash = hasher("test.txt")
    print("Hash before signing: " + hash)

    # 3. Sign the file
    sign = signer("test.txt", "G39")

    # 4. Hash the file after signing
    hash = hasher("test.txt")
    print("Hash after signing:  " + hash)

    # 5. Remove the testing file
    os.remove("test.txt")