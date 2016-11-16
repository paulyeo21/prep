class Hash
  def initialize length
    @keys = Array.new(length)
    @values = Array.new(length)
  end

  def []=(key, value)
    hash_value = hash_function(key)
    @keys[hash_value] = key
    @values[hash_value] = value
  end

  def [](key)
    hash_value = hash_function(key)
    @values[hash_value]
  end

  def to_s
    puts @keys.inspect
    puts @values.inspect
  end

  def length
    @keys.length
  end

  private

  def hash_function value
    value % length
  end
end

def main
  hash = Hash.new(5)
  hash[1] = "a" 
  hash[2] = "b" 
  puts hash[1]
  puts hash
end

# main
