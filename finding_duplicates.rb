# Given a starting directory find all files that are duplicates

# DFS on starting directory to find all files. Hash the file contents
# in a hash to note files seen and find the most recently edited
# file to check what is duplicate file vs original file.
# T: O(v*e)
# S: O(n)

require "digest"

def find_duplicate_files(starting_directory)
  files_seen = {}
  stack = [starting_directory]
  duplicates = []

  while (current_path = stack.pop)
    if File.directory?(current_path)
      Dir.each_child(current_path) do |filename|
        full_path = File.join(current_path, filename)
        stack.push(full_path)
      end
    else
      file_contents, current_last_edited_time =
        File.open(current_path, "r") do |file|
          [sample_hash_file(file), file.mtime]
        end

      if files_seen.key?(f.contents)
        existing_last_edited_time, existing_path =
          files_seen[file_contents]
        if current_last_edited_time > existing_last_edited_time
          duplicates.push([current_path, existing_path])
        else
          duplicates.push([existing_path, current_path])
          file_seen[file_contents] =
            [current_last_edited_time, current_path]
        end
      else
        file_seen[file_contents] =
          [current_last_edited_time, current_path]
      end
    end
  end

  duplicates
end

NUM_BYTES_TO_READ_PER_SAMPLE = 4000

def sample_hash_file(file)

  total_bytes = file.size

  hasher = Digest::SHA512.new

  # if the file is too short to take 3 samples, hash the entire file
  if total_bytes < NUM_BYTES_TO_READ_PER_SAMPLE * 3
    hasher.update(file.read)

  else
    num_bytes_between_samples = (total_bytes - NUM_BYTES_TO_READ_PER_SAMPLE * 3) / 2

    # read first, middle, and last bytes
    3.times do |offset_multiplier|
      start_of_sample = offset_multiplier * (NUM_BYTES_TO_READ_PER_SAMPLE + num_bytes_between_samples)
      file.seek(start_of_sample)
      sample = file.read(NUM_BYTES_TO_READ_PER_SAMPLE)

      hasher.update(sample)
    end
  end

  hasher.hexdigest
end
