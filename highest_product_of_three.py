# Given a list of integers, find the highest product
# you can get from three of the integers.

# T: O(n)
# S: O(1)
def highest_product_of_three(list_of_ints):
# 1. Track highest positive, highest negative, and second highest positive.
# 2. At every index, if current number is negative, compute product with highest negative
#    and highest positive. Else, compute product with highest positive and second highest
#    positive. 
    highest = max(list_of_ints[:3])
    lowest = min(list_of_ints[:3])
    if list_of_ints[0] > list_of_ints[1]:
        if list_of_ints[2] > list_of_ints[0]:
            second_highest = list_of_ints[0]
        elif list_of_ints[1] > list_of_ints[2]:
            second_highest = list_of_ints[1]
        else:
            second_highest = list_of_ints[2]
    elif list_of_ints[1] > list_of_ints[2]:
        second_highest = list_of_ints[2]
    else:
        second_highest = list_of_ints[1]
    second_lowest = second_highest

    product = highest * lowest * second_highest
    for i in xrange(3, len(list_of_ints)):
        # print 'highest %s' % highest
        # print 'lowest %s' % lowest
        # print 'second %s' % second_highest
        current = list_of_ints[i]
        product = max(product, current * lowest * highest, \
                current * highest * second_highest, \
                current * lowest * second_lowest)

        if current > highest:
            second_highest = highest
            highest = current
        elif current < lowest:
            second_lowest = lowest
            lowest = current
        elif current > second_highest:
            second_highest = current
        elif current < second_lowest:
            second_lowest = current

    return product

def highest_product_of_three(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_two = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_two = list_of_ints[0] * list_of_ints[1]
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in xrange(2, len(list_of_ints)):
        current = list_of_ints[i]
        highest_product_of_three = max(highest_product_of_three,
                                       current * highest_product_of_two,
                                       current * lowest_product_of_two)
        highest_product_of_two = max(highest_product_of_two,
                                     current * highest,
                                     current * lowest)
        lowest_product_of_two = min(lowest_product_of_two,
                                    current * lowest,
                                    current * highest)
        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_three

print highest_product_of_three([1,2,3,3]) # 18
print highest_product_of_three([-3,2,3,4,-5]) # 60
print highest_product_of_three([3,-2,-3,-4,5]) # 60
print highest_product_of_three([-10,-10,1,3,2]) # 300
