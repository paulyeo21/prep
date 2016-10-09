def two_sum(array, sum):
    sums = {}
    for i in range(len(array)):
        number = array[i]
        if number in sums:
            return [sums[number], i] 
        else:
            sums[sum - number] = i

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([5, 7, 11, 15], 18))
