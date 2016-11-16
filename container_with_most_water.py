def maxArea(heights):
    max_area = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        length = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, length * height)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_area

print(maxArea([1, 1]))
print(maxArea([0, 2]))
print(maxArea([0, 0, 2]))
print(maxArea([5, 0, 2]))
print(maxArea([1, 2, 1]))
