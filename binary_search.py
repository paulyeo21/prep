def binarySearch(arr, k):
    if not arr:
        return None

  left = 0
  right = len(arr)

  while left < right:
      mid = (left + right) / 2

    if k == arr[mid]:
        left_i = mid - 1
      right_i = mid + 1

      while left_i >= 0:
          if arr[left_i] != k:
              break
        left_i -= 1

      while right_i <= len(arr)-1:
          if arr[right_i] != k:
              break
        right_i += 1

      return (left_i + 1, right_i - 1)

  elif k < arr[mid]:
      right = mid
  else:
      left = mid + 1

  return (None, None)
