class Queue
  def initialize
    @queue = []
  end

  def push item
    @queue << item
  end

  def pop
    @queue.delete_at(0)
  end

  def empty?
    @queue.length == 0
  end

 def to_s
   @queue.inspect
 end
end

def main
  queue = Queue.new

  puts "Initial: #{queue}"

  queue.push(1)
  puts "Push: 1"
  puts "Queue: #{queue}"

  queue.push(2)
  puts "Push: 2"
  puts "Queue: #{queue}"

  queue.push(3)
  puts "Push: 3"
  puts "Queue: #{queue}"

  puts "Popped: #{queue.pop}"
  puts "Queue: #{queue}"

  queue.push(4)
  puts "Push: 4"
  puts "Queue: #{queue}"

  puts "Popped: #{queue.pop}"
  puts "Queue: #{queue}"
end

# main
