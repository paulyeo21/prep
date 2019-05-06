# Given a full deck of cards represented by an array
# of integers range 1..52, and two halves half1 and half2
# check if the full deck is a single riffle of the two halves.

# not a single riffle if: 
# cards from a half are out of order in full deck. for instance,
# a half has Jack of Clubs and then Jack of Spades, then we expect 
# full deck to have those in order.
# T: O(n)
# S: O(n) #recursion
def is_single_riffle_deck(full_deck, half1, half2)
  # check if top card of deck is either on half1 or half2
  # if it is then remove that card from deck and then from corresponding
  # half. else false. repeat until deck is empty.
  if full_deck.empty?
    return true
  elsif half1 and full_deck.last == half1.last
    full_deck.pop
    half1.pop
    return is_single_riffle_deck(full_deck, half1, half2)
  elsif half2 and full_deck.last == half2.last
    full_deck.pop
    half2.pop
    return is_single_riffle_deck(full_deck, half1, half2)
  else
    return false
  end
end

# T: O(n)
# S: O(1)
def is_single_riffle_deck(deck, half1, half2)
  i, j, k = 0, 0, 0
  while i < deck.length
    if half1 and deck[i] == half1[j]
      j += 1
    elsif half2 and deck[i] == half2[k]
      k += 1
    else
      return false
    end
    i += 1
  end
  true
end

puts is_single_riffle_deck([1,2,3], nil, [1,2,3])
puts is_single_riffle_deck([2,1,3], [1,2], [3])
