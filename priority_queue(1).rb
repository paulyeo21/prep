class PriorityQueue
  def initialize
    @queue = [0]
  end

  # We represent binary tree by an array where a parent at index i has children that
  # are less in value at indices 2i and 2i + 1. The tree must be 1) complete binary tree
  # which means that all levels are full except for the last and 2) must keep with max
  # heap property meaning the parent nodes must be greater than children nodes. When we
  # insert value we append to the back of the array, which already gives us 1) since we
  # are either completing a level of the tree or adding to the last level. The max heap
  # property can be met by swapping the insert node with its subsequent parent nodes
  # until the property is met. This requires at most the number of operations to swap
  # with the root, which is log2 n.
  # T: O(log n)
  def <<(val)
    insert(val)
  end

  def insert(val)
    @queue.push(val)
    i = @queue.length - 1
    swap = (i % 2 == 0 ? i / 2 : (i - 1) / 2)
    while @queue[swap] < val and swap != 0
      temp = @queue[swap]
      @queue[swap] = val
      @queue[i] = temp
      i = swap
      swap = (i % 2 == 0 ? i / 2 : (i - 1) / 2)
    end
  end

  # Similar to insert, but we want to remove the top most node which is index at 1. We
  # swap that with the last node in the array and propagate the root down until it meets
  # heap property. At most the node will be propagated all the way down to the last
  # element which will take at most log2 n operations.
  # T: O(log n)
  def pop
    temp = @queue.pop
    output = @queue[1]
    @queue[1] = temp
    i = 1
    swap = 2*i
    while @queue[swap] and @queue[i] < @queue[swap]
      temp = @queue[i]
      @queue[i] = @queue[swap]
      @queue[swap] = temp
      i = swap
      swap = 2*swap
    end
    return output
  end

  def empty?
    @queue.length == 1
  end
  
  def to_s
    @queue.inspect
  end
end

pq = PriorityQueue.new
pq.insert(5)
pq << 1
pq << 1
pq << 5
puts pq.pop
puts pq
puts pq.pop
puts pq
puts pq.pop
