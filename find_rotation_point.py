# Given a list of words, return index of the alphabetically first word.

# T: O(lg n)
# S: O(lg n)
def find_rotation_point(words):
    # use binary search
    return find_rotation_point_helper(words, 0, len(words)-1)

def find_rotation_point_helper(words, left, right):
    # base case: if words[left] < words[right] or words[mid] < words[mid-1]
    # we know we're at wrong half if words[left] < words[right]
    mid = (left + right)/2

    if words[left] <= words[right]:
        return left
    elif words[mid] > words[right]:
        return find_rotation_point_helper(words, mid+1, right)
    else:
        return find_rotation_point_helper(words, left, mid)

# T: O(lg n)
# S: O(1)
def find_rotation_point(words):
    left, right = 0, len(words)-1

    while True:
        mid = (left + right)/2

        if words[left] <= words[right]:
            return left
        elif words[mid] > words[right]:
            left = mid + 1
        else:
            right = mid

# def find_rotation_point(words):
#     first_word = words[0]
#     floor, ceiling = 0, len(words) - 1

#     while floor < ceiling:
#         guess_index = floor + ((ceiling - floor) / 2)

#         if words[guess_index] >= first_word:
#             floor = guess_index
#         else:
#             ceiling = guess_index

#         if floor + 1 == ceiling:
#             return ceiling

print find_rotation_point(['a', 'b', 'c']) # 0
print find_rotation_point(['c', 'a', 'b']) # 1
print find_rotation_point(['b', 'c', 'a']) # 2
print find_rotation_point(['ptolemaic',
                           'retrograde',
                           'supplant',
                           'undulate',
                           'xenoepist',
                           'asymptote',
                           'babka',
                           'banoffee',
                           'engender',
                           'karpatka',
                           'othellolagkage'
                          ]) # 5
