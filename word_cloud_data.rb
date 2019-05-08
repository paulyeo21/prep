# Given a long text build a hash of words to occurrences.

def word_cloud(text)
  # 1. split the words from the input string
  # 2. populate the hash with each word
  # 3. handle words that are both uppercase and lowercase
  # consider pronouns
  # consider nouns at start of sentences
  # consider punctuation
  word_counts = {}
  end_of_word_delimiter = [",", ":", ".", " ", ";", "?", "!"]
  start_of_word, i = 0, 0
  while i < text.length
    if end_of_word_delimiter.include?(text[i])
      if word_counts.key?(text[start_of_word..i-1])
        word_counts[text[start_of_word..i-1]] += 1
      else
        word_counts[text[start_of_word..i-1]] = 1
      end
      start_of_word = i + 1
    end
    i += 1
  end
  word_counts.inspect
end

puts word_cloud("After beating the eggs, Dana read the next step:\
                Add milk and eggs, then add flour and sugar.") #
