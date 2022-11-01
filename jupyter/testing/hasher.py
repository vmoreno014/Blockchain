# Generates the hash for a given filename
import hashlib
import os


def hasher(file):
    with open(file, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        return hashlib.sha256(bytes).hexdigest()


# TESTING

# 1. Create a file
file = open("test.txt", "w")
file.write("Hello World")
file.close()

# 2. Hash the file
hash = hasher("test.txt")

# 3. Print the hash
print(hash)

# 4. Remove the testing file
os.remove("test.txt")