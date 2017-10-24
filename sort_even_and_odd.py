# Given an array sort all the elements in even positions in ascending order
# and odd positions in descending order

def sortEvenAndOdd(arr):
    evens = arr[::2]
    odds = arr[1::2]
    increasingEvens = sorted(evens)
    decreasingOdds = sorted(odds, reverse = True)
    output = []

    for i in range(max(len(increasingEvens), len(decreasingOdds))):
        output.append(increasingEvens[i])
        output.append(decreasingOdds[i])
    return output

print(sortEvenAndOdd([2, 3, 1, 5])) # [1, 5, 2, 3]
