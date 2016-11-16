def max_xor(numbers):
    xor = numbers[0]
    for number in numbers[1:]:
        # xor = xor | number
    return xor

print(max_xor([3, 10, 5, 25, 2, 8]))
