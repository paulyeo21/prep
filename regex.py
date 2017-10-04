# Create a function that checks if a string matches a given regex

def isMatch(string, regex):
    if not string:
        return True
    if not regex:
        return False
    else:
        if len(regex) > 1 and regex[1] == "*":
            return isMatch(string, regex[2:]) or isMatch(string[1:], regex)
        else:
            if string[0] == regex[0] or regex[0] == ".":
                return isMatch(string[1:], regex[1:])
            if string[0] != regex[0]:
                return False


assert isMatch("aa", "a.") == True
assert isMatch("aa", "a") == False
assert isMatch("aaa", "a*") == True
assert isMatch("aaab", "a*b") == True
assert isMatch("", "a*") == True
