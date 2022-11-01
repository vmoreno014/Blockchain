import checker
import basics

new_block = "SGSSI-22.CB.03.txt"
old_block = "SGSSI-22.CB.02.VMOR.txt"

status = checker.checker(new_block, old_block)
hash1 = basics.hasher(new_block)
hash2 = basics.hasher(old_block)

print(hash1)
print(hash2)
print(status)