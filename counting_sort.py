def countingSort(numbers, k):
    counts = [0 for i in range(k)]
    for number in numbers:
        counts[number] += 1

    increment = counts[0]
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_numbers = [0 for i in range(len(numbers))]
    for number in numbers:
        index = counts[number]
        counts[number] -= 1
        sorted_numbers[index - 1] = number

    return sorted_numbers

assert countingSort([1, 4, 1, 2, 7, 5, 2], 9) == [1, 1, 2, 2, 4, 5, 7]
