from timeit import default_timer as timer
import random
import time
import hashlib
import basics


def block_miner(text, digits):
    n = 1
    ntext = text
    while hashlib.sha256(ntext.encode('utf-8')).hexdigest()[0:digits] != "0" * digits:
        n += 1
        ntext = f'{text} {n}'

    return n, hashlib.sha256(ntext.encode("utf-8")).hexdigest()


if __name__ == '__main__':
    ZEROS_REQUIRED = 12
    filename = "SGSSI-22.CB.04.txt"

    for i in range(0, ZEROS_REQUIRED + 1):
        sign = basics.signer(filename, "G39")

        with open(filename, "r") as f:
            text = f.read()

        start = time.perf_counter()
        iters, hash = block_miner(text, i)
        end = time.perf_counter()

        print(f'Hash try {iters:20,} in {end - start:7.4f} seconds => {hash}')
