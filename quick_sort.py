# Quicksort
# T: O(n log n)
# S: O(1)

def quickSort(numbers):
    quickSortUtil(numbers, 0, len(numbers) - 1)

def quickSortUtil(numbers, left, right):
    if left < right:
        p = partition(numbers, left, right, numbers[0])
        print numbers, left, right, p
        quickSortUtil(numbers, 0, p)
        quickSortUtil(numbers, p, len(numbers) - 1)

def partition(numbers, left, right, pivot):
    print numbers, left, right, pivot

    while numbers[left] < pivot and left <= right:
        left += 1

    while numbers[right] >= pivot and right >= left:
        right -= 1
    
    if left >= right:
        numbers[0] = numbers[right]
        numbers[right] = pivot
        return right
    else:
        temp = numbers[left]
        numbers[left] = numbers[right]
        numbers[right] = temp
        return partition(numbers, left, right, pivot)


print quickSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
