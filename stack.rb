class Stack
  def initialize
    @stack = []
    @length = 0 
  end

  def push item
    @stack << item
    @length += 1 
  end

  def pop
    @stack.pop
  end

  def to_s
    @stack.inspect
  end

  def empty?
    @stack.length == 0
  end
end

def main
  stack = Stack.new

  puts "Initialize: #{stack}"

  stack.push(5)
  puts "Pushed: 5"
  puts "Stack: #{stack}"

  stack.push(4)
  puts "Pushed: 4"
  puts "Stack: #{stack}"

  puts "Pop: #{stack.pop}"
  puts "Stack: #{stack}"
end

# main
