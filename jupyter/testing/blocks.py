import os
import shutil
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

# CASE 3: Signs and hashes a file
def test_case3():
    # 1. Create a file
    file = open("test.txt", "w")
    file.write("Hello World")
    file.close()

    # 2. The file before signing
    with open("test.txt", "r") as f:
        lines = f.readlines()
        print("Before signing: " + str(lines))

    # 3. Hash the file
    hash = block_hasher("test.txt", "G39")

    # 4. Print the hash
    print("Hash: " + hash)

    # 4. The file after signing
    with open("test.txt", "r") as f:
        lines = f.readlines()
        print("After signing:  " + str(lines))

    # 5. Remove the file
    os.remove("test.txt")

