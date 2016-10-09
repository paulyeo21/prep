def recursive_string_permutations(string)
  index = 0
  recursive_string_permutations_util(string, index)
end

def recursive_string_permutations_util(string, i)
  if i < string.length-1
    permutations = recursive_string_permutations_util(string, i+1)

    current_permutations = []
    for permutation in permutations
      (0..permutation.length).each do |j|
        current_permutations << "#{permutation[0, j]}#{string[i]}#{permutation[j, permutation.length]}"
      end
    end

    return current_permutations
  else
    [string[i]]
  end
end

puts recursive_string_permutations("civ")
