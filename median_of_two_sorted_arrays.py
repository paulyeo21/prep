# O(n+m)
# def median_of_two_sorted_arrays(numbers1, numbers2):
#     i, j, k = 0, 0, 0
#     numbers = []
#     while i < len(numbers1) and j < len(numbers2):
#         if numbers1[i] < numbers2[j]:
#             numbers.append(numbers1[i])
#             i += 1
#         else:
#             numbers.append(numbers2[j])
#             j += 1
#         k += 1

#     while i < len(numbers1):
#         numbers.append(numbers1[i])
#         i += 1
#         k += 1

#     while j < len(numbers2):
#         numbers.append(numbers2[j])
#         j += 1
#         k += 1

#     # If even return mean of two middles
#     if len(numbers) % 2 == 0:
#         mid = len(numbers) / 2
#         return (numbers[mid] + numbers[mid - 1]) / 2.0
#     # Else odd return mid number
#     else:
#         return numbers[len(numbers) / 2]

# O(log(n+m))
def median(numbers):
    if numbers:
        # If even return mean of two middles
        if len(numbers) % 2 == 0:
            mid = len(numbers) / 2
            return (numbers[mid] + numbers[mid - 1]) / 2.0

        # Else odd return mid number
        else:
            return numbers[len(numbers) / 2]
    else:
        return None

def lower_half(numbers):
    if numbers:
        mid = len(numbers) / 2
        if len(numbers) % 2 == 0:
            return numbers[:mid]
        else:
            return numbers[:mid+1]
    else:
        return []

def upper_half(numbers):
    if numbers:
        return numbers[len(numbers) / 2:]
    else:
        return []

def median_of_two_sorted_arrays(numbers1, numbers2):
    median1 = median(numbers1)
    median2 = median(numbers2)
    
    if not median1:
        return median2

    elif not median2:
        return median1

    elif median1 == median2:
        return median1

    elif len(numbers1) == 1 and len(numbers2) == 1:
        return median(numbers1 + numbers2)

    else:
        if median1 > median2:
            return median_of_two_sorted_arrays(lower_half(numbers1), upper_half(numbers2))

        else:
            return median_of_two_sorted_arrays(upper_half(numbers1), lower_half(numbers2))

print(median_of_two_sorted_arrays([], [1, 2]))
print(median_of_two_sorted_arrays([1, 3], [2]))
print(median_of_two_sorted_arrays([1, 2], [3, 4]))
print(median_of_two_sorted_arrays([1,2,3], [4,5,6]))
print(median_of_two_sorted_arrays([1], [2,3]))

