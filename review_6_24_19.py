# 6. Check if any permutation of a string is a palindrome.

# Clarifications:
#   a) Given 'baba' return True
#   b) Given 'abc' return False
# Edge cases:
#   a) Given '' return True
#   b) Given 'a' return True
#   c) Given 'ab' return False
#   d) Given None return None
# Algorithms:
#   a) Get all permutations and check each if palindrome exists. T: O(n!) S: O(n!)
#   b) Count characters and see if all duplicates or all duplicates except one
#      character. T: O(n) S: O(n)

def permutationPalindrome(string):
    if string == None:
        return None

    if len(string) == 0:
        return True

    uniqueCharacters = set()
    for char in string:
        if char in uniqueCharacters:
            uniqueCharacters.remove(char)
        else:
            uniqueCharacters.add(char)

    return len(uniqueCharacters) == 1 or \
            len(uniqueCharacters) == 0

assert(permutationPalindrome('') == True)
assert(permutationPalindrome(None) == None)
assert(permutationPalindrome('a') == True)
assert(permutationPalindrome('ab') == False)
assert(permutationPalindrome('baba') == True)
assert(permutationPalindrome('abc') == False)

# 7. Implement merge sort

# Clarifications:
#   a) Given an array return a sorted array using merge sort
#   b) Can you be given an empty array? Yes.
#   c) Can you be given None? No.
#   d) Should we handle duplicate numbers? Yes.
# Edge cases:
#   a) Given [] return []
#   b) Given [1,1,1,1] return [1,1,1,1]
#   c) Given [8,1,3,2] return [1,2,3,8]
# Algorithms:
#   a) Recursively split array into two subarrays. Split until array length is
#      1. When length is 1, compare the two subarrays and merge them according
#      to sort order. Return merged array. T: O(n lg n) S: O(n)

def mergeSort(arr, left_i, right_i):
    if not arr:
        return arr

    if left_i == right_i:
        return [arr[left_i]]

    mid = (left_i + right_i) / 2
    left = mergeSort(arr, left_i, mid)
    right = mergeSort(arr, mid + 1, right_i)

    i, j = 0, 0
    output = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    while i < len(left):
        output.append(left[i])
        i += 1

    while j < len(right):
        output.append(right[j])
        j += 1

    return output

assert(mergeSort([], 0, 0) == [])
assert(mergeSort([1,1,1,1], 0, 3) == [1,1,1,1])
assert(mergeSort([8,1,3,2], 0, 3) == [1,2,3,8])

# 8. Implement count sort

# Clarifications:
#   a) Given an array of integers with a max, return sorted array in T: O(n).
#   b) Can we be given an empty array? Yes.
#   c) Can we be given a None? Yes.
# Edge cases:
#   a) Given [] return []
#   b) Given None return None
#   c) Given [3,2,1,100,20], 100 return [1,2,3,20,100]
# Algorithms:
#   a) Create an array of length equal to the max. The value at each index
#      represents the count of the number of the index in the given array.
#      Now count down from the max (or up depending on sort order) and for
#      each count that exists in the count order append to output. T: O(k + n) S: O(k + n)

def countSort(arr, maximum):
    if not arr:
        return arr

    counts = [0] * (maximum + 1)
    for integer in arr:
        counts[integer] += 1

    output = []
    for number in range(1, maximum + 1):
        count = counts[number]

        for _ in range(count):
            output.append(number)

    return output

assert(countSort([],0) == [])
assert(countSort(None,0) == None)
assert(countSort([3,2,1,100,20],100) == [1,2,3,20,100])

# 9. Given an array of prices find the max profit where a[j] - a[i] and i < j.

# Clarifications:
#   a) Find the max difference between two integers where the first integer must
#      in order before the second.
#   b) Can there be negative numbers? Yes.
#   c) Can there be zeros? Yes.
#   d) Can we be given an empty array? Yes.
#   e) Can we be given a None? Yes.
# Edge cases:
#   a) Given [4,4,10,20,3] return 20 - 4 = 16
#   b) Given [4,-4,10,20,3] return 20 - (-4) = 24
#   c) Given [] return 0
#   d) Given None return 0
# Algorithms:
#   a) Iterate over integers and also store previous minimum. Compare difference
#      between current and previous and check if greater than current greatest
#      difference. If greater than store as current greatest difference. If current
#      is smaller than minimum, store current as minimum. T: O(n) S: O(1)

def maxProfit(arr):
    if not arr:
        return 0

    if len(arr) < 2:
        return 0

    if len(arr) == 2:
        return arr[1] - arr[0]

    minimum = min(arr[1], arr[0])
    maximum = arr[1] - arr[0]
    for i in range(2, len(arr)):
        maximum = max(arr[i] - minimum, maximum)
        minimum = min(arr[i], minimum)

    return maximum

assert(maxProfit([]) == 0)
assert(maxProfit(None) == 0)
assert(maxProfit([1]) == 0)
assert(maxProfit([4,4,10,20,3]) == 16)
assert(maxProfit([4,-4,10,20,3]) == 24)
