"""
A number x in a list of integers is called lonely if no other number y in the list satisfies |x-y| <= k. That is, each other number differs from a lonely number by more than k. For example, if k=10, the only lonely number in the list {1,30,47,1,20,17} is 47.

A list of integers is called happy if there are no lonely numbers in the list.

A sublist of a list is a contiguous subsequence of the list. For example, {3,4,5} is a sublist of {1,2,3,4,5,6}, but {2,4,6} is not a sublist of {1,2,3,4,5,6}.

You are given a list of integers (in a format that is specified below) and an m. Find and return the smallest k such that the given list has a happy sublist of length at least m.

The list of integers is provided in the following way: You are given an len, a init, and s a, b, c, and d. Use the following pseudocode to generate the list:

input: len, init, a, b, c, d.

arr = array of length len
for i = 0,...,len(init)-1:
   arr[i] = init[i]
for i = len(init),...,len-1:
   arr[i] = (arr[i-1] * a + b * i + c) % d
"""
class FindingFriends:
    def generateList(self, length, init, a, b, c, d):
        arr = [None] * length
        for i in range(len(init)):
            arr[i] = init[i]
        for i in range(len(init), length):
            arr[i] = (arr[i - 1] * a + b * i + c) % d
        return arr

    def happy(self, lst, k):
        for i in range(len(lst)):
            current = lst[i]
            unhappy = True
            for j in range(len(lst)):
                if i == j:
                    continue
                if current - k == lst[j] or current + k == lst[j]:
                    unhappy = False
            if unhappy:
                return False
        return True

    def shortestDistance(self, length, init, a, b, c, d, m):
        lst = self.generateList(length, init, a, b, c, d)
        print "Generated array is", lst

        k = 0
        while True:
            # Generate sublists and check if 'happy' and length of m
            for i in range(length):
                for j in range(i, length):
                    sublist = lst[i:j + 1]
                    if len(sublist) >= m and self.happy(sublist, k):
                        print(sublist)
                        return k
            k += 1
        return False

finding_friends = FindingFriends()
print(finding_friends.shortestDistance(6, [8, 1, 10, 2, 9, 7], 12, 34, 56, 78, 2))
print(finding_friends.shortestDistance(7, [1], 1, 0, 0, 12345678, 5))
print(finding_friends.shortestDistance(12, [0], 1, 0, 1, 6, 3))
print(finding_friends.shortestDistance(10, [3, 4, 5], 23, 34, 35, 46, 4))
# print(finding_friends.shortestDistance(2, [0, 1000000000], 0, 0, 0, 1, 2))
# print(finding_friends.shortestDistance(5, [1, 2, 1000, 3, 4], 9, 8, 7, 10, 3))

