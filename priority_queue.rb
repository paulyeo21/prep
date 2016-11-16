class PriorityQueue
  def initialize
    @queue = [0]
  end

  def <<(element)
    @queue << element
    percolate_up(@queue.size - 1)
  end

  def pop
    # Exchange first and last
    max = @queue[1]
    @queue[1] = @queue[size - 1]
    @queue.pop

    # Reorder the root node after exchanging
    percolate_down(1)

    # Pop last element
    max
  end

  def empty?
    @queue.length == 1
  end

  def to_s
    @queue.inspect
  end

  private

  def percolate_up(index)
    while index > 1
      parent = index / 2

      if @queue[parent] > @queue[index]
        # element is in the right place
        return
      else
        # Swap 
        tmp = @queue[parent]
        @queue[parent] = @queue[index]
        @queue[index] = tmp
        index = index / 2
      end
    end 
  end

  def percolate_down(index)
    while index * 2 < @queue.length - 1 
      # Find greater child node
      child, child_index = max_with_index(@queue[index * 2], @queue[index * 2 + 1])

      # Check if child node is greater than current
      if child > @queue[index]
        # Swap
        @queue[child_index] = @queue[index]
        @queue[index] = child 
      else
        # Current node is in right place
        return
      end
    end
  end

  def max_with_index(first, second)
    if @queue[first] > @queue[second]
      return @queue[first], first
    else
      return @queue[second], second
    end
  end

  def size
    @queue.length
  end
end

def main
  pq = PriorityQueue.new
  pq << 1
  pq << 2
  pq << 3
  puts pq
  puts pq.pop
  puts pq
  puts pq.pop
  puts pq
end

# main
