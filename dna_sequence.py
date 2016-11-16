import numpy

class DnaSequence:
    def __init__(self, pattern):
        self.pattern = pattern
        self.end = len(pattern)
        self.alphabet = self.create_alphabet()
        self.index_of = self.create_index_of_map()
        self.transitions = self.create_transitions_table()

    def create_alphabet(self):
        alphabet = []
        for char in self.pattern:
            if char not in alphabet:
                alphabet.append(char)
        return alphabet

    def create_index_of_map(self):
        hmap = {}
        for i in range(len(self.alphabet)):
            hmap[self.alphabet[i]] = i
        return hmap

    def create_transitions_table(self):
        transitions = numpy.zeros((len(self.pattern) + 1, len(self.alphabet)))

        for x in range(len(self.pattern)):
            for y in range(len(self.alphabet)):
                # Compose input string
                string = self.pattern[:x] + self.alphabet[y]

                # Match the last few characters of the string with the string pattern
                # to see how many characters we have already read in.
                # i.e. if the composed string is "aaba" then check if "aaba" matches
                # if not then move on to "_aba", then "__ba", then "___a".
                for z in range(len(string)):
                    if string[z:] == self.pattern[:len(string)-z]:
                        transitions[x, y] = x + 1 - z
                        break
                    z -= 1

        return transitions

    def search(self, genome):
        state = 0
        for char in genome:
            if char in self.index_of:
                state = int(self.transitions[state, self.index_of[char]])
                if state == self.end:
                    return True
            else:
                state = 0
        return False

dna_sequence = DnaSequence("CAT") 
print(dna_sequence.search("ACCATGCA")) # => True
print(dna_sequence.search("CATTGA")) # => True
print(dna_sequence.search("GGCACACATG")) # => True
print(dna_sequence.search("CAAT")) # => False

dna_sequence = DnaSequence("AABAC") 
print(dna_sequence.search("AABCAAABAABACCBA")) # => True

