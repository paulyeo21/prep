require "../data-structures/stack.rb"
require "../data-structures/binary_tree_node.rb"

def depth_first_search(root)
  stack = Stack.new
  stack.push(root)

  while not stack.empty?
    current = stack.pop
    puts current.value

    if current.right
      stack.push(current.right)
    end

    if current.left
      stack.push(current.left)
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

depth_first_search(a)
