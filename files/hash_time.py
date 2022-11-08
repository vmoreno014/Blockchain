import secrets
from timeit import default_timer as timer
import random
import time
import hashlib
import basics
import shutil
import os

def block_miner(filename, digits):
    n = 0
    tmp = "a"

    while tmp[0:digits] != "0" * digits:
        if os.path.exists("copy.txt"):
            os.remove("copy.txt")
        copy = shutil.copyfile(filename, "copy.txt")

        f = open(copy, "a")
        sign = "\n" + secrets.token_hex(4) + " G39"
        f.write(sign)
        f.close()

        with open(copy, "rb") as f:
            bytes = f.read()  # read entire file as bytes
            tmp = hashlib.sha256(bytes).hexdigest()
        n = n + 1

    return n, tmp, sign


if __name__ == '__main__':
    ZEROS_REQUIRED = 12
    filename = "SGSSI-22.CB.04.txt"

    for i in range(1, ZEROS_REQUIRED + 1):
        with open(filename, "r") as f:
            text = f.read()

        start = time.perf_counter()
        iters, hash, sign = block_miner(filename, i)
        end = time.perf_counter()

        print(f'Hash try {iters:20,} in {end - start:7.4f} seconds => {hash}')

