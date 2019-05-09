# Given a list of integers where: 1) integers are in the range 1..n.
# 2) the length of the list is n+1. 3) list has at least one integer
# which appears at least twice but it can have several duplicates,
# and each duplicate may appear more than twice, find an integer
# that appears more than once in our list. Optimize for space.

# Naive solution is to use a hash. To optimize for space we can
# do O(n**2) by iterating twice to find a duplicate. Even better
# would be to sort and then iterate to find duplicates next to each
# other. If we don't want to destroy the input we do the following:

# T: O(n lg n)
# S: O(1)
def find_repeat(ints):
    # Given that our list of ints has at least one duplicate int
    # and that the range of ints is limited to 1..n with n + 1 being
    # the length of the list, we know that there are less distinct
    # numbers for a sublist than possible. For instance, if we were given
    # [1,2,3,4,4] we see that the number of distinct ints is 4 while the possible
    # distinct ints 4, but if we look at sublists [1,2] and [3,4,4]
    # we see that for [1,2] the possible distinct ints is 2 and the
    # actual distinct ints is 2, but for [3,4,4] the possible distinct
    # ints is 3 and the actual distinct ints is 3. So there must be
    # a duplicate. We do this until we are left with list of size 1.

    left, right = 1, len(ints) - 1
    while left < right:
        mid = (left + right) / 2
        lower_number_of_possible_distinct = mid - left + 1
        upper_number_of_possible_distinct = right - mid

        lower_number_of_actual_distinct = 0
        for num in ints:
            if num >= left and num <= mid:
                lower_number_of_actual_distinct += 1

        if lower_number_of_actual_distinct > lower_number_of_possible_distinct:
            right = mid
        else:
            left = mid + 1

    return left

# def find_repeat(the_list):
#     floor = 1
#     ceiling = len(the_list) - 1

#     while floor < ceiling:
#         # Divide our range 1..n into an upper range and lower range
#         # (such that they don't overlap)
#         # Lower range is floor..midpoint
#         # Upper range is midpoint+1..ceiling
#         midpoint = floor + ((ceiling - floor) / 2)
#         lower_range_floor, lower_range_ceiling = floor, midpoint
#         upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

#         # Count number of items in lower range
#         items_in_lower_range = 0
#         for item in the_list:
#             # Is it in the lower range?
#             if item >= lower_range_floor and item <= lower_range_ceiling:
#                 items_in_lower_range += 1

#         distinct_possible_integers_in_lower_range = (
#             lower_range_ceiling
#             - lower_range_floor
#             + 1
#         )
#         if items_in_lower_range > distinct_possible_integers_in_lower_range:
#             # There must be a duplicate in the lower range
#             # so use the same approach iteratively on that range
#             floor, ceiling = lower_range_floor, lower_range_ceiling
#         else:
#             # There must be a duplicate in the upper range
#             # so use the same approach iteratively on that range
#             floor, ceiling = upper_range_floor, upper_range_ceiling

#     # Floor and ceiling have converged
#     # We found a number that repeats!
#     return floor

print find_repeat([3, 2, 1, 1, 4]) # 1
print find_repeat([1, 2, 3, 5, 5, 5]) # 5
print find_repeat([4, 2, 3, 1, 1]) # 1
