require "../data-structures/binary_search_tree_node.rb"

def kth_largest_in_bst(k, node)
  count = 0
  kth_largest_util(k, node, count)
end

def kth_largest_util(k, node, c)
  return if not node or c >= k
  puts "initial: #{c}"
  kth_largest_util(k, node.right, c)
  c += 1
  puts "after: #{c}"
  puts
  return node.value if k == c 
  kth_largest_util(k, node.left, c)
end

a = BinarySearchTreeNode.new(1)
b = BinarySearchTreeNode.new(2)
c = BinarySearchTreeNode.new(3)

b.left = a
b.right = c

puts kth_largest_in_bst(3, b)
