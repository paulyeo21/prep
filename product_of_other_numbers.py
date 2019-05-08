# Given a list of integers, for each index you want to find
# the product of every integer except the integer at that index
# without using division.

# Naive method is to iterate list for each index, with say
# two while loops. When i == j don't compute otherwise,
# take product. Append to output. This would be T: O(n**2) S: O(n)


# Do two passes. First pass going forward, as iterating over ints, store product
# of previous ints up to index. Same going backwards. For instance, given
# [1,7,3,4]. Forward: [1,1,1*7,1*7*3] and backward: [7*3*4,3*4,4,1]. Now
# output is the product at each index: [1*7*3*4,1*3*4,1*7*4,1*7*3*1]
# T: O(n)
# S: O(n)
def get_products_of_all_ints_except_at_index(list_of_ints):
    if len(list_of_ints) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    output = [1] * len(list_of_ints)

    product_up_to_i = list_of_ints[0]
    for i in xrange(1, len(list_of_ints)):
        output[i] = product_up_to_i
        product_up_to_i *= list_of_ints[i]

    product_up_to_i = list_of_ints[len(list_of_ints)-1]
    for i in xrange(len(list_of_ints)-2, -1, -1):
        output[i] *= product_up_to_i
        product_up_to_i *= list_of_ints[i]

    return output

print get_products_of_all_ints_except_at_index([1,7,3,4]) # [7*3*4, 1*3*4, 1*7*4, 1*7*3] = [84,12,28,21]
print get_products_of_all_ints_except_at_index([0,7,3,4]) # [7*3*4, 0*3*4, 0*7*4, 0*7*3] = [84,0,0,0]
