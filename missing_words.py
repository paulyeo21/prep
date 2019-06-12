
def missingWords(s, t):
    i, j = 0, 0
    output = []
    skip_this_word = False
    current_word = ''

    while i < len(s):
        print i, j, current_word, output

        if (j == 0 or j == len(t)) and s[i] == ' ':
            if not skip_this_word:
                output.append(current_word)
            skip_this_word = False
            current_word = ''
            j += 1

        if j < len(t) and s[i] == t[j]:
            j += 1
            skip_this_word = True

        current_word += s[i]
        i += 1

    return output

print missingWords('I am using hackerrank to improve programming', 'am hackerrank to improve')
