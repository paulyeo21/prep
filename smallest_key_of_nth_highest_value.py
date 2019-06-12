# Complete a function that returns the smallest key (sorted in ascending order alphabetically) of the given input dictionary containing nth highest value

# For example:  
#           - dictionary : {"a":1, "b": 2, "c": 100, "d": 30}
#           - n : 2 (2nd highest value)
#
#           - output : "d"

# max heap
# iterate over dictionary, add (key, value) to max heap ~ O(m)
# return nth heap entry: O(n log k)
import heapq

def return_key(input_dict,n):
    if n > len(input_dict):
        return None

    heap = []

    for k, v in input_dict.items():
        heapq.heappush(heap, (v, k))

    for _ in range(len(input_dict) - n):
        heapq.heappop(heap)

    if len(heap) == 0:
        return None
    else:
        return heapq.heappop(heap)[1]

assert return_key({},1) == None
assert return_key({"a": 10,"b": 20},0) == None
assert return_key({"a": 1,"b": 2,"c": 3,"d": 4,"e": 5},6) == None
assert return_key({"a": 10,"b": 20,"c": 3,"d": 2,"e": 9},1) == 'b'
assert return_key({"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999},2) == 'laptop'
print('passed')
