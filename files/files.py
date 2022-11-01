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