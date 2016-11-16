import numpy

def cost(str1, str2):
    if str1 == str2:
        return 0
    else:
        return 1

def minimum_edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    else:
        edit = minimum_edit_distance(str1[1:], str2[1:]) + cost(str1[0], str2[0])
        insert = minimum_edit_distance(str1[1:], str2) + 1
        delete = minimum_edit_distance(str1, str2[1:]) + 1
        return min(edit, insert, delete)

# print(minimum_edit_distance("cat", "at"))
# print(minimum_edit_distance("abcdef", "azced"))

def memoized_minimum_edit_distance_utility(str1, str2, memo):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    else:
        edit = memoized_minimum_edit_distance_utility(str1[1:], str2[1:], memo) + cost(str1[0], str2[0])
        insert = memoized_minimum_edit_distance_utility(str1[1:], str2, memo) + 1
        delete = memoized_minimum_edit_distance_utility(str1, str2[1:], memo) + 1

        minimum_cost = min(edit, insert, delete)
        memo[(str1, str2)] = minimum_cost
        return minimum_cost

def memoized_minimum_edit_distance(str1, str2):
    memo = {}
    return memoized_minimum_edit_distance_utility(str1, str2, memo)

# print(memoized_minimum_edit_distance("789", "123456789"))

def dp_minimum_edit_distance(str1, str2):
    matrix = numpy.zeros((len(str1) + 1, len(str2) + 1))

    for i in range(len(str1) + 1):
        matrix[i][0] = i

    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Compare each substring of str1 to substring of str2
    # and fill in matrix corresponding to substring matches
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            substr1 = str1[:i]
            substr2 = str2[:j]
            if substr1[-1] == substr2[-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                # Find minimum of modify, edit, delete
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1

    return matrix[len(str1)][len(str2)]

print(dp_minimum_edit_distance("789", "123456789"))
print(dp_minimum_edit_distance("abcdef", "azced"))
