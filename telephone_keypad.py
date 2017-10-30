# Get the combination of keypad characters given a number

keypad = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def keypadCombinations(number):
    combinations = []
    return keypadCombinationsUtil(number, combinations, "")

def keypadCombinationsUtil(number, combinations, string):
    strNumber = str(number)
    if not number:
        combinations.append(string)
        return combinations
    for char in keypad[strNumber[0]]:
        keypadCombinationsUtil(strNumber[1:], combinations, string + char)
    return combinations

def keypadCombinations1(number):
    strNumber = str(number)
    if not number:
        return [""]
    combos = []
    for char in keypad[strNumber[0]]:
        for combo in keypadCombinations1(strNumber[1:]):
            combos.append(char + combo)
    return combos


print(keypadCombinations(1))
print(keypadCombinations(2))
print(keypadCombinations(23))
print(keypadCombinations1(23))
