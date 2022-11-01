import filecmp
import re

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

                # checks every line except the last one and the two first lines
                for i in range(len(lines1) - 1):
                    if i < 3:
                        continue

                    if lines1[i] != lines2[i]:
                        print("Different line (", i, "):\n", lines1[i], lines2[i])
                        return False

                # checks the last line
                if not re.match(r"[a-z0-9]{8} G([0-9]{2})+", lines2[-1]):
                    return False

    # check if the hash of the second file starts with zeros
    hash = basics.hasher(path_input2)
    if not hash.startswith("00"):
        return False

    return True


# CASE 6: Checks if two files accomplish the requirements
def test_case6():
    path_input1 = "SGSSI-22.CB.02.txt"
    path_input2 = "SGSSI-22.CB.02.VMOR.txt"
    print("Valid file: ", checker(path_input1, path_input2))

# TESTING
# test_case6()
