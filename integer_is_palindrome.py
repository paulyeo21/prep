# T: O(n)
# S: O(1)
def isPalindrome(integer):
    if integer < 0:
        return False

    if integer == 0:
        return True

    # Check from left side and right side
    nth_place = 1
    while integer / nth_place > 9:
        nth_place *= 10

    while integer != 0:
        left = integer / nth_place
        right = integer % 10
        if left != right:
            return False
        else:
            integer = (integer % nth_place) / 10
            nth_place /= 100
    
    return True

print(isPalindrome(101))
print(isPalindrome(233))
print(isPalindrome(121))
print(isPalindrome(-155))
