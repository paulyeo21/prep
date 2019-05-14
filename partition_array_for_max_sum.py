# 1043. Partition Array for Maximum Sum

# Given a list of integers, partition the list into contiguous
# subarrays of length at most K. After partitioning, each subarray
# has their values changed to the max value in the subarray.
# Return the largest sum of list after partitioning.

def maxSumAfterPartitioning(A, K):
    # if k == 1 return sum of original
    # if k == 2 and say list is [1,3,4] you should partition to [1,3]
    # and [4] so that 1 -> 3, but if list is [3,1,4], it should be
    # [3], [1,4]. 

    # At A[i] find max int from A[i] to A[i+k], replace

# print maxSumAfterPartitioning([1,15,7,9,2,5,10], 3) # [15,15,15,9,10,10,10] 84
# print maxSumAfterPartitioning([9,15,7,1,2,5,10], 3) # [9,15,15,15,10,10,10] 84
print maxSumAfterPartitioning([1,10], 1) # 11
print maxSumAfterPartitioning([1,3,4], 2) # [3,3,4] 10
print maxSumAfterPartitioning([3,1,4], 2) # [3,4,4] 11
