import secrets
import hashlib
import os
import shutil
import time


# Sign the file with an 8-len HEX string and a signature
def signer(file, signature):
    f = open(file, "a")
    sign = secrets.token_hex(4) + " " + signature
    f.write(sign + "\n")
    f.close()
    return sign


# Generates the hash for a given filename
def hasher(file):
    with open(file, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        return hashlib.sha256(bytes).hexdigest()


# Number of zeros to string
def convert_string(n):
    zeros = ""
    for i in range(n):
        zeros += "0"

    return zeros


# Returns the hash from a signed block
def block_hasher(path, signature):
    # Makes a copy of the input file
    copy = shutil.copyfile(path, "signed.txt")
    signed, _ = signer(copy, signature)  # file 'signed.txt' is now signed
    signed_hash = hasher(signed)             # hash of the signed file
    os.remove(copy)           # removes the copy
    return signed_hash


# Finds a hash with a given number of zeros
def num_finder(file, signature, n_zeros):
    zeros = convert_string(n_zeros)

    while True:
        signed_hash = block_hasher(file, signature)
        if signed_hash.startswith(zeros):
            return file, signed_hash


# Finds the maximum number of zeros under the given time
# We can't use num_finde because process can take more time than the given seconds
def max_finder(path_input, path_output, signature, seconds):
    max_zeros = 1
    zeros = convert_string(max_zeros)

    copy = shutil.copyfile(path_input, "tmp.txt")
    valid_hash = ""
    t = 0
    start = time.time()

    while t < seconds:
        t = time.time() - start
        signed_hash = block_hasher(copy, signature)

        if signed_hash.startswith(zeros):
            valid_hash = signed_hash

            if os.path.exists(path_output):
                os.remove(path_output)

            shutil.copyfile(copy, path_output)
            os.remove(copy) # resets the file to remove the last signature
            copy = shutil.copyfile(path_input, "tmp.txt")
            max_zeros += 1
            zeros = convert_string(max_zeros)

    return valid_hash


# Searches for a hash from the input file, that starts with a given number of zeros
# and copies the signed file to the output file
def file_signer(path_input, path_output, signature, n_zeros):
    copy = shutil.copyfile(path_input, "tmp.txt")
    zeros = convert_string(n_zeros)

    while True:
        signed_hash = block_hasher(copy, signature)
        if signed_hash.startswith(zeros):
            shutil.copyfile(copy, path_output)
            os.remove(copy)
            return signed_hash


def tester():
    # File to sign
    path = "SGSSI-22.CB.01.txt"
    # Signature to add
    signature = "G39"
    # Time to find the maximum number of zeros
    seconds = 20

    # Finds the maximum number of zeros under the given time
    hash = max_finder(path, "output1.txt", signature, seconds)
    print("Hash: {}".format(hash))

    # Finds a hash with a given number of zeros
    _, hash = num_finder(path, signature
                         , 1)
    print("Hash: {}".format(hash))

    # Searches for a hash from the input file, that starts with a given number of zeros
    # and copies the signed file to the output file
    hash = file_signer(path, "output2.txt", signature, 1)
    print("Hash: {}".format(hash))

tester()
print("TESTING FINISHED")
