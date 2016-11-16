class TestTaking:
    def findMax(self, questions, guessed, actual):
        correct = min(actual, guessed)
        correct += min(questions - actual, questions - guessed)
        return correct

test_taking = TestTaking()
print(test_taking.findMax(3, 1, 2))
print(test_taking.findMax(3, 2, 1))
print(test_taking.findMax(5, 5, 0))
print(test_taking.findMax(10, 8, 8))
