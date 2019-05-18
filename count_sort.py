# Counting sort is efficient if we know the bounds of our integers.

def countingSort(numbers, k):
    # 1. Create two empty lists. One to hold the sorted integers
    # and another to hold the counts of each integer in a list
    # from 0 to k.
    # 2. Iterate over unsorted numbers and track counts in before
    # mentioned list.
    # 3. Decrement/Increment depending on whether decreasing or
    # increasing output from bounds (k to 0 or 0 to k) and if
    # count exists, add number to output for each count occurence.
    # T: O(k + n) where k is the bound (highest possible integer)
    # S: O(k + n)

    counts = [0] * (k + 1)
    output = []

    for num in numbers:
        counts[num] += 1

    for i in range(k, -1, -1):
        count = counts[i]

        for _ in range(count):
            output.append(i)

    return output

print countingSort([1, 4, 1, 2, 7, 5, 2], 9) #
