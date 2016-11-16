require "../data-structures/queue.rb"
require "../data-structures/binary_tree_node.rb"

def breadth_first_search(root)
  queue = Queue.new
  queue.push(root)

  while not queue.empty?
    current = queue.pop
    puts current.value

    if current.left
      queue.push(current.left)
    end

    if current.right
      queue.push(current.right)
    end
  end
end

a = BinaryTreeNode.new(1)
b = BinaryTreeNode.new(2)
c = BinaryTreeNode.new(3)
d = BinaryTreeNode.new(4)

a.left = b
a.right = c

b.right = d

breadth_first_search(a)
