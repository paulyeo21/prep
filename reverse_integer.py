def reverse_integer(integer):
    output = ""
    string = str(integer)

    if string[0] == "-":
        isNegative = True
        string = string[1:]
    else:
        isNegative = False

    i = len(string) - 1
    while i >= 0:
        output += string[i]
        i -= 1

    if isNegative:
        if -int(output) < (~(1 << 31)):
            return 0
        else:
            return int(output)
    else:
        if int(output) > (1 << 31):
            return 0
        else:
            return int(output)

print(reverse_integer(123))
print(reverse_integer(100))
print(reverse_integer(-123))
print(reverse_integer(1534236469))
print(reverse_integer(-2147483648))
