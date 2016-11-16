def atoi(string):
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    # Strip white space and -/+
    string_integer = ""
    isNegative = False
    signExists = False # Case "-+12" returns 0
    integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in string:
        if char == " " and not string_integer and not signExists:
            continue
        elif char == "-":
            if signExists:
                return 0
            else:
                isNegative = True
                signExists = True
        elif char == "+":
            if signExists:
                return 0
            else:
                isNegative = False
                signExists = True
        elif char in integers:
            string_integer += char
        else:
            break

    # Convert string to integer
    nth_place = 1
    length = len(string_integer) - 1
    integer = 0
    while length >= 0:
        integer += int(string_integer[length]) * nth_place 
        nth_place *= 10
        length -= 1

    if isNegative:
        if -integer <= ~(1 << 31):
            return MIN_INT
        else:
            return -integer
    else:
        if integer >= (1 << 31):
            return MAX_INT
        else:
            return integer

print(atoi("300"))
print(atoi("  13"))
print(atoi("3  "))
print(atoi(" "))
print(atoi("-15"))
print(atoi("2147483648"))
print(atoi("-2147483649"))
print(atoi("  -0012a42"))
print(atoi("-+2"))
print(atoi("  +0 123"))
print(atoi("  - 321"))

