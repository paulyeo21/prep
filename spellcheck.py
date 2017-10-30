"""
Given a string, return the spellchecked version of the string. Could be correctly spelled. Assume we are given a dictionary of correctly spelled words.
"""

import random
import editdistance
import string

# corpus = corpus.txt
# process corpus into data structure

corpus = {}

def spellCheck(string):
    spellCheckedWords = []
    bestScore = float('inf')
    for word, _ in corpus.iteritems():
        localBest = editdistance.eval(string, word)
        if bestScore > localBest:
            # print bestScore, localBest, word
            bestScore = localBest
            spellCheckedWords = [word]
        elif bestScore == localBest:
            spellCheckedWords.append(word)
    return spellCheckedWords

# dictionary = {"ba": True, "bb": True}

def stripNumbers(string):
    return filter(lambda x: x.isalpha(), string)

assert stripNumbers("a12b") == "ab"

def main():
    f = open("sherlock_holmes.txt")
    for line in f:
        for word in line.split():
            clean = stripNumbers(word.strip(string.punctuation))
            if clean not in corpus:
                corpus[clean] = True
main()
# corpus["ba"] = True
# corpus["bb"] = True
# corpus.pop("b")

print len(corpus)
print spellCheck("b")
