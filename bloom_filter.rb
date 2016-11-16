class BloomFilter
  def initialize
    @items = Array.new(10) # Arbitrary size
  end

  def push(item)
    index = hash(item)
    @items[index] = 1
  end

  def [](item)
    index = hash(item)
    @items[index] ? true : false
  end

  private

  def hash(key)
    key % 10 # An actual hashing implementation...
  end
end

def main
  bloom_filter = BloomFilter.new
  bloom_filter.push(0)
  bloom_filter.push(1)
  puts bloom_filter[0]
  puts bloom_filter[2]
end

main
