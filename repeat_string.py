import math

class RepeatString:
    def minimalModify(self, string):
        half = int(math.ceil(float(len(string)) / 2))
        a, b = string[:half], string[half:]

        mismatches = 0
        for i in range(half):
            if i < len(a) and i < len(b):
                if a[i] != b[i]:
                    mismatches += 1
        return mismatches + abs(len(a) - len(b))
       

repeat_string = RepeatString()
print(repeat_string.minimalModify("aba"))
print(repeat_string.minimalModify("adam"))
print(repeat_string.minimalModify("x"))
print(repeat_string.minimalModify("aaabbbaaaccc"))
print(repeat_string.minimalModify("repeatstring"))
print(repeat_string.minimalModify("aaaaaaaaaaaaaaaaaaaa"))
