import numpy

class Solution:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.longest_x = 0
        self.longest_y = 0
        self.matrix = self.build_matrix()

    def build_matrix(self):
        matrix = numpy.zeros((len(self.first), len(self.second))) 

        # Compare each character of first string to each character of second string
        # If they match then store the length of the longest common 
        #   substring of the previous characters for the first and second strings + 1
        # Else store 0
        # i.e. abcdaf vs zbcdf
        #   Compare a_____ vs z____, _b____ vs z____, __c___ vs z____, and so on 
        #   when comparing a_____ vs _b___, _b____ vs _b____, then find the length of
        #   the common substring for a_____ vs z____ and + 1
        for i in range(len(self.first)):
            char_of_first = self.first[i]

            for j in range(len(self.second)):
                char_of_second = self.second[j]

                if char_of_first == char_of_second:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    if matrix[i][j] > matrix[self.longest_x][self.longest_y]:
                        self.longest_x = i
                        self.longest_y = j
                else:
                    matrix[i][j] = 0

        return matrix

    def longest_common_substring(self):
        x = self.longest_x
        y = self.longest_y
        length = self.matrix[x][y]
        substring = ""

        while length > 0:
            substring = self.first[x] + substring
            x -= 1
            y -= 1
            length = self.matrix[x][y]

        return substring

# solution = Solution("abcdaf", "zbcdf")
# print(solution.longest_common_substring())

def brute_force_longest_common_substring(str1, str2):
    longest = ""
    length = 0
    for a in range(1, len(str1) + 1):
        for b in range(1, len(str2) + 1):
            if str1[:a] == str2[:b]:
                if len(str1[:a]) > length:
                    length = len(str1[:a])
                    longest = str1[:a]
    return longest

# print(brute_force_longest_common_substring("abc", "ab"))
