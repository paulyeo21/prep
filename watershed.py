# Given a matrix with numbers, find all the different watersheds.
# For instance:
# Input: [[4,5,3,4,5],[3,3,4,5,3],[2,4,9,9,8],[7,8,1,0,6]]
# Output: [(0,2),(1,4),(2,0),(3,3)]

# 1. Iterate over each point in matrix
# 2. For each point in matrix, check each direction
#    as well as diagonals to see if current is smallest.
# 3. If smallest, then add index to output.

def watershed(matrix):
    if len(matrix) == 0:
        return []

    if len(matrix) == 1: # if one row
        # iterate over row and check sides

    if len(matrix[0]) == 1: # if one col
        # iterate over col and check sides

    output = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            # check all directions (incl. diagonals)
            # we need to also check if directions are valid indices

            current = matrix[i][j]
            min_neighbor = current

            # up: i-1
            if i-1 >= 0 and i-1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i-1][j])
            # down: i+1
            if i+1 >= 0 and i+1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i+1][j])
            # right: j+1
            if j+1 >= 0 and j+1 <= cols-1:
                min_neighbor = min(min_neighbor, matrix[i][j+1])
            # left: j-1
            if j-1 >= 0 and j-1 <= cols-1:
                min_neighbor = min(min_neighbor, matrix[i][j-1])
            # diagonal-up-left: i-1,j-1
            if j-1 >= 0 and j-1 <= cols-1 and i-1 >= 0 and i-1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i-1][j-1])
            # diagonal-up-right: i-1,j+1
            if j+1 >= 0 and j+1 <= cols-1 and i-1 >= 0 and i-1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i-1][j+1])
            # diagonal-down-left: i+1,j-1
            if j-1 >= 0 and j-1 <= cols-1 and i+1 >= 0 and i+1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i+1][j-1])
            # diagonal-down-right: i+1,j+1
            if j+1 >= 0 and j+1 <= cols-1 and i+1 >= 0 and i+1 <= rows-1:
                min_neighbor = min(min_neighbor, matrix[i+1][j+1])

            if min_neighbor == current:
                output.append((i,j))

    return output

print(watershed([[4,5,3,4,5],[3,3,4,5,3],[2,4,9,9,8],[7,8,1,0,6]]))
print(watershed([4,5,3,1]))
print(watershed([[4,5,3,1]]))
print(watershed([]))
