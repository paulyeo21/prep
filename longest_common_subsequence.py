import numpy

class Solution:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.matrix = self.build_matrix()

    def build_matrix(self):
        matrix = numpy.zeros((len(self.first), len(self.second))) 

        # Compare substring of first string vs substring of second string
        for i in range(len(self.first)):
            current = self.first[:i+1]
            for j in range(len(self.second)):
                compare = self.second[:j+1]

                # If last character of current string and the comparison string
                # are the same, then increment 1
                if current[len(current)-1:] == compare[len(compare)-1:]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        return matrix

    def longest_common_subsequence(self):
        x = len(self.first) - 1
        y = len(self.second) - 1
        subsequence = ""
        length = self.matrix[x][y]

        # Walk back to find the subsequence
        while x >= 0 and y >= 0:
            length = self.matrix[x][y]
            if self.first[x:x+1] == self.second[y:y+1]:
                subsequence = self.first[x:x+1] + subsequence
                x -= 1
                y -= 1
            else:
                if self.matrix[x-1][y] == length:
                    x -= 1
                elif self.matrix[x][y-1] == length:
                    y -= 1
                length = self.matrix[x][y]

        return subsequence

solution = Solution("acbcf", "abcdaf")
print(solution.longest_common_subsequence())

