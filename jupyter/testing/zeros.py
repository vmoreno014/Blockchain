import os
import shutil
import blocks
import basics


# Number of zeros to string
def __convert_string(n):
    zeros = ""
    for i in range(n):
        zeros += "0"

    return zeros


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
            os.remove(copy)
            return signed_hash

# CASE 4: Finds a hash with a given number of zeros
def test_case4():
    # 1. Create a file
    file = open("test.txt", "w")
    file.write("Hello World")
    file.close()

    # 2. Hash the file
    hash = blocks.block_hasher("test.txt", "G39")

    # 3. Print the hash
    print("Hash of the file with signature G39:\n" + hash)

    # 4. Find a hash with 2 zeros
    hash = num_finder("test.txt", "G39", 2)

    # 5. Print the hash
    print("\nHash same file but with different private key (8 length hex string) starts with at least 2 zeros:\n" + hash)

    # 6. Remove the file
    os.remove("test.txt")

