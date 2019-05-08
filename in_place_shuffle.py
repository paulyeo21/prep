# Given a list, do an in-place shuffle. The shuffle must be
# "uniform," meaning each item in the original list must
# have the same probability of ending up in each spot in the
# fina list.

import random

def in_place_shuffle(ints):
    for i in xrange(len(ints)-1):
        j = random.randint(i, len(ints)-1)
        ints[j], ints[i] = ints[i], ints[j]
    return ints

print in_place_shuffle([1,2,3])
