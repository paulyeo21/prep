# 1. Given an array of ranges such as [[0, 1], [1, 2]] return a range that condenses ranges that overlap.

# Clarification: 
#   a) Given the sample input array the return value should be [[0, 2]].
#   b) Can you be given a range where y >= x? No.
#   c) Is input given in an order? No.
# Edge cases:
#   a) Given ranges that don't overlap such as [[0, 1], [2, 3]] would return [[0, 1], [2, 3]]
#   b) Given an undefined range [], returns []
#   c) Given a range that spans other ranges such as [[0, 9], [1, 2], [2, 3], [10, 11]] returns [[0, 9], [10, 11]]
#   d) If number of ranges < 2, return input
# Algorithms:
#   a) 1. Sort ranges by x. For each range pair such as a and b, check if b_x <= a_y if so then merge ranges by taking
#         a_x and max of a_y and b_y. T: O(n lg n) S: O(n)

def condenseRanges(ranges):
    if len(ranges) < 2:
        return ranges

    ranges = sorted(ranges)
    output = []
    previous = ranges[0]
    for i in range(1, len(ranges)):
        current = ranges[i]
        if current[0] > previous[1]: # if b_x is > a_y (not overlapping)
            output.append(previous)
            previous = current
        else:
            previous = [previous[0], max(previous[1], current[1])]

    output.append(previous) # append last range
    return output

assert(condenseRanges([]) == [])
assert(condenseRanges([[1, 2]]) == [[1, 2]])
assert(condenseRanges([[1, 2], [2, 3]]) == [[1, 3]])
assert(condenseRanges([[1, 2], [3, 4]]) == [[1, 2], [3, 4]])
assert(condenseRanges([[1, 6], [3, 4]]) == [[1, 6]])

# 2. Reverse a string in place.

# Clarifications:
#   a) Given 'abcd' return 'dcba'
#   b) You expect space complexity to be O(1)? Yes.
# Edge cases:
#   a) Given '' return ''
#   b) Given None return None
# Algorithms:
#   a) Iterate over characters in string and swap out index offset from beginning
#      with index offset from end. For example, given 'abcd' when iterating
#      you would first swap 'dbca'. T: O(n) S: O(1)

def reverseString(string):
    if not string:
        return string

    arr = list(string) # python does not allow string char assignment
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return ''.join(arr)

assert(reverseString('') == '')
assert(reverseString(None) == None)
assert(reverseString('abc') == 'cba')
assert(reverseString('abcd') == 'dcba')

# 3. Given a sentence with words, reverse the words.

# Clarification:
#   a) Given something such as "don't eat peppercorns" return "peppercorns eat don't"
#   b) Can you be given punctuation? Yes.
#   c) What are the non-alphabetic characters we should be aware of? .,'-?!
# Edge Cases:
#   a) Given '' return ''
#   b) Given None return None
# Algorithms:
#   a) 1. Reverse the whole string. Such as given "don't eat" you would get "tae t'nod" and then 
#         by splitting across white space reverse each individual word so ["tae", "t'nod"] would
#         become ["eat", "don't"]. T: O(n) S: O(1)

def reverseWords(sentence):
    def reverseStringInPlace(arr, left, right):
        if not arr:
            return

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if not sentence:
        return sentence

    if len(sentence) == 1:
        return sentence

    reverseStringInPlace(sentence, 0, len(sentence)-1)
    starting = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            reverseStringInPlace(sentence, starting, i-1)
            starting = i+1

        if i == len(sentence)-1: # if last word then wont hit empty space
            reverseStringInPlace(sentence, starting, i)

a = ['']
reverseWords(a)
assert(a == [''])

b = None
reverseWords(b)
assert(b == None)

c = ['d','o','n',"'",'t',' ','e','a','t',' ','p','e','p','p','e','r','c','o','r','n','s']
reverseWords(c)
assert(c == ['p','e','p','p','e','r','c','o','r','n','s',' ','e','a','t',' ','d','o','n',"'",'t'])

# 4. Merge two sorted arrays

# Clarifications:
#   a) Given [1,2,3,4] and [2,3,4] return [1,2,2,3,3,4]
#   b) Can you be given an empty array? Yes.
#   c) Can you be given a None? No.
# Edge cases:
#   a) Given [] and [1,2,3] return [1,2,3]
#   b) Given [1,2,3] and [4,5,6] return [1,2,3,4,5,6]
# Algorithms:
#   a) Have three pointers, one for array a, the other for array b, and the last for the array holding
#      the merged arrays c. Iterate over the greater length of a and b, and compare between element of a 
#      and element of b. If element of a is less than add to output array c and increment pointer for array
#      a. Lastly check increment pointers for a and b until greater than lengths of a and b while appending
#      element to output. T: O(n + m) S: O(n + m)

def mergeTwoSortedArrays(a, b):
    if not a:
        return b
    if not b:
        return a

    i, j = 0, 0
    output = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1

    while i < len(a):
        output.append(a[i])
        i += 1

    while j < len(b):
        output.append(b[j])
        j += 1

    return output

assert(mergeTwoSortedArrays([], [1,2,3]) == [1,2,3])
assert(mergeTwoSortedArrays([1,2,3,4], [2,3,4]) == [1,2,2,3,3,4,4])
assert(mergeTwoSortedArrays([1,2,3], [4,5,6]) == [1,2,3,4,5,6])

# 4. Merge k sorted arrays

# Clarifications:
#   a) Given [[1,2,3],[1],[2]] return [1,1,2,2,3]
#   b) Can you be given no arrays? Yes
#   c) Can there be a None? No.
# Edge cases:
#   a) Given duplicates, should include duplicates in merged array
#   b) When one array is exhausted, we should still sort merge the rest of the arrays
# Algorithms:
#   a) 1. Transform each array into a linked list. 2. Use a priority queue to store and sort
#         the linked lists by values, then when pop and append to output array. 3. When popping
#         insert the linked list if next value exists back into queue. T: O(k * n lg n) S: O(n lg n)

import operator

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class PriorityQueue:
    def __init__(self, isMaxHeap=True):
        self.values = [None]
        self.length = 0
        self.isMaxHeap = isMaxHeap

    def pop(self):
        if self.length == 0:
            return Error('No elements to pop')
        output = self.values[1]
        self.values[1] = self.values[self.length]
        self.values.pop() # get rid of extra space
        self.length -= 1
        self.percolateDown(1)
        return output

    def push(self, value):
        self.values.append(value)
        self.length += 1
        self.percolateUp(self.length)

    def compare(self, obj1, obj2, op):
        return op(obj1.value, obj2.value)

    def percolateDown(self, i):
        left = i * 2
        right = i * 2 + 1

        if self.isMaxHeap:
            leftOp = operator.lt
            rightOp = operator.gt
        else:
            leftOp = operator.gt
            rightOp = operator.lt

        if left < self.length + 1 and self.compare(self.values[i], self.values[left], leftOp):
            self.values[i], self.values[left] = self.values[left], self.values[i]
            self.percolateDown(left)
        if right < self.length + 1 and self.compare(self.values[i], self.values[right], rightOp):
            self.values[i], self.values[right] = self.values[right], self.values[i]
            self.percolateDown(right)

    def percolateUp(self, i):
        parent = i / 2

        if self.isMaxHeap:
            op = operator.gt
        else:
            op = operator.lt

        if parent > 0 and self.compare(self.values[i], self.values[parent], op):
            self.values[i], self.values[parent] = self.values[parent], self.values[i]
            self.percolateUp(parent)

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        output = []
        for obj in self.values:
            if obj:
                output.append(obj.value)
        return str(output)

# pq = PriorityQueue(False)
# pq.push(Node(1))
# pq.push(Node(2))
# pq.push(Node(3))
# pq.push(Node(4))
# print(pq)
# pq.pop()
# print(pq)
# pq.pop()
# print(pq)

def mergeKSortedArrays(arrs):
    def arrayToLinkedList(arr):
        head = Node(None)
        current = head
        for element in arr:
            current.next = Node(element)
            current = current.next
        return head.next

    if len(arrs) == 0:
        return arrs

    pq = PriorityQueue(False)
    for arr in arrs:
        pq.push(arrayToLinkedList(arr))

    output = []
    while not pq.isEmpty():
        current = pq.pop()
        output.append(current.value)
        if current.next:
            pq.push(current.next)

    return output

assert(mergeKSortedArrays([]) == [])
assert(mergeKSortedArrays([[1],[2,3]]) == [1,2,3])
assert(mergeKSortedArrays([[1,2,3],[1],[2]]) == [1,1,2,2,3])
# assert(mergeKSortedArrays([[2,2,2],[1],[2],[2,3,4],[5,6,7]]) == [1,2,2,2,2,2,3,4,5,6,7])

# 5. Given an array of integers and a sum, find two integers that make sum.

# Clarifications:
#   a) What do we do if there are multiple pairs of integers that add to sum? Return either.
#   b) Are we guaranteed two integers?
# Edge cases:
#   a) If no two integers add to sum, return None.
#   b) Given [1,2,3,4] and sum 5, return (1,4) or (2,3).
# Algorithms:
#   a) Use a hash map to save time. While iterating over integers add to hash map the difference
#      between sum and current number. As iterating if the integer exists in hash, then we know
#      that we have found a pair, so return current element and the difference. T: O(n) S: O(n)

def findPairOfIntsThatSum(ints, _sum):
    if not ints:
        return None

    hashMap = {}
    for _int in ints:
        if _int in hashMap:
            return (_sum - _int, _int)
        else:
            hashMap[_sum - _int] = True

    return None

assert(findPairOfIntsThatSum([], 0) == None)
assert(findPairOfIntsThatSum([1,2,3,4], 0) == None)
assert(findPairOfIntsThatSum([1,-1], 0) == (1, -1))
assert(findPairOfIntsThatSum([1,2,3,4], 5) == (2, 3))
