# Given a deck (represented by an array of integers) and
# two halves (half1 and half2) which are also array of ints,
# Find if the deck is made of a single riffle shuffle of
# the two halves. 

# We know that if you riffle, the order of the cards in the
# halves must be preserved by the deck. So we want to check
# each card in deck and check if the order is preserved.

# T: O(n)
# S: O(n)
def is_possibly_single_riffle(deck, half1, half2):
    # 1. Get top card on deck.
    # 2. Is it top card on half1 or half2? If so,
    #    Repeat. Else, not a single riffle.
    if len(deck) != len(half1) + len(half2):
        raise ValueError('Number of cards in deck must equal '
                         'number of cards in halves.')
    if not deck:
        return True
    elif deck[len(deck)-1] == half1[len(half1)-1]:
        half1.pop()
        deck.pop()
    elif deck[len(deck)-1] == half2[len(half2)-1]:
        half2.pop()
        deck.pop()
    else:
        return False
    return is_possibly_single_riffle(deck, half1, half2)

# T: O(n)
# S: O(1)
def is_possibly_single_riffle(deck, half1, half2):
    if len(deck) != len(half1) + len(half2):
        raise ValueError('Number of cards in deck must equal '
                         'number of cards in halves.')
    i, j, k = 0, 0, 0
    while i < len(deck):
        if j < len(half1) and deck[i] == half1[j]:
            j += 1
        elif k < len(half2) and deck[i] == half2[k]:
            k += 1
        else:
            return False
        i += 1

    return True

print is_possibly_single_riffle(range(1,52), range(1,52), [])
print is_possibly_single_riffle([], range(1,52), [])
