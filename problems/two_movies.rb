def two_movies(desired_length, movie_lengths)
  past_movies = {}
  for current_movie in movie_lengths
    if past_movies[desired_length - current_movie]
      return true
    else
      past_movies[current_movie] = true
    end
  end

  false
end

movie_lengths = [1, 2, 4, 5]
desired_length = 8
puts two_movies(desired_length, movie_lengths)
