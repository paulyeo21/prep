# Write a recursive function that accepts an integer which is the
# number of digits and prints all binary numbers that have exactly that
# many digits in ascending order.

def allBinary(n):
    # For each existing binary number (['']) if none, add
    # 0 or 1. T: O(2**n), S: O(2**n)
    if n == 0:
        return ['']

    binaries = allBinary(n-1)

    new_binaries = []
    for x in ['0','1']:
        for binary in binaries:
            new_binaries.append(x + binary)

    return new_binaries

print allBinary(0) # []
print allBinary(1) # [0,1]
print allBinary(2) # [00,01,10,11]
print allBinary(3) # [000,001,010,011,100,101,110,111]
