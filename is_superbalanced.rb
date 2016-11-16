require "../data-structures/binary_tree_node.rb"

def is_superbalanced(root)
  stack = [] # (node, h)
  stack.push([root, 1])

  heights = []

  while not stack.empty?
    current, h = stack.pop

    if not current.left and not current.right
      if !heights.include? h
        heights.push(h)

        if heights.length > 2 or (heights.length == 2 and (heights[0] - heights[1]).abs > 1)
          return false
        end
      end
    end

    if current.left
      stack.push([current.left, h+1])
    end

    if current.right
      stack.push([current.right, h+1])
    end
  end

  return true
end

a = BinaryTreeNode.new(1)
b = BinaryTreeNode.new(2)
c = BinaryTreeNode.new(3)
d = BinaryTreeNode.new(4)
e = BinaryTreeNode.new(5)
f = BinaryTreeNode.new(6)
g = BinaryTreeNode.new(7)
h = BinaryTreeNode.new(8)
i = BinaryTreeNode.new(9)

a.left = b
a.right = c
b.left = d

e.left = f
e.right = i
f.left = g
g.left = h

puts is_superbalanced(a)
puts is_superbalanced(e)
