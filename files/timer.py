import os
import shutil
import time

import blocks
import basics
import zeros


# Number of zeros to string
def __convert_string(n):
    zeros = ""
    for i in range(n):
        zeros += "0"

    return zeros

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
        copy = shutil.copyfile(path_input, "mf_tmp.txt")



    os.remove(copy)
    return valid_hash

# CASE 5: Find the maximum number of zeros under the given time
def test_case5():
    # input file
    f = open("input.txt", "w")
    f.write("Hello World!")
    f.close()
    path_input = "input.txt"

    # output file
    path_output = "output.txt"

    # signature
    signature = "ikaslea"

    # time in seconds
    seconds = 3
    print("Search time: " + str(seconds) + " seconds")

    # hash with the maximum number of zeros
    hash = max_finder(path_input, path_output, signature, seconds)


    # print the hash
    print("Hash: " + hash)

    # print the last line of the output file
    with open(path_output, "r") as f:
        print("Last line of the output file: " + f.readlines()[-1])

    # remove the files
    os.remove(path_input)
    os.remove(path_output)

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


def test_lab6():
    path_input = "SGSSI-22.CB.03.txt"
    path_output = "SGSSI-22.CB.03.VMOR.txt"
    signature = "G39"
    seconds = 60
    print("Search time: " + str(seconds) + " seconds")

    hash = max_finder(path_input, path_output, signature, seconds)
    print("Hash: " + hash)

    with open(path_output, "r") as f:
        print("Last line of the output file: " + f.readlines()[-1])

# TESTING
"""
print(" --- CASE 1 --- ")
basics.test_case1()

print("\n --- CASE 2 --- ")
basics.test_case2()

print("\n --- CASE 3 --- ")
blocks.test_case3()
# First part, can be understood as a private key (since it is not shared)
# Second part, can be understood as a public key (since is an input parameter, so it can be know by the user)

print("\n --- CASE 4 --- ")
zeros.test_case4()

print("\n --- CASE 5 --- ")
test_case5()

print("\n --- LAB 5 --- ")
test_lab5()


"""

print("\n --- LAB 6 --- ")
test_lab6()
