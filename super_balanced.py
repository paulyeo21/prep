# Given a binary tree, check if the tree is superbalanced.
# Superbalanced means the difference in depths between
# any two leaf nodes is no greater than one. 

import binary_tree_node

def is_superbalanced(root):
    # DFS while noting height. Use DFS because can short circuit earlier.
    # If more heights than 3 or if two heights and difference is greater 
    # than 1, not superbalanced.
    frontier = [(root, 0)]
    heights = []

    while len(frontier):
        current, height = frontier.pop()

        if not current.left and not current.right:
            if height not in heights:
                heights.append(height)

            if len(heights) > 2:
                return False
            if len(heights) == 2 and abs(heights[0] - heights[1]) > 1:
                return False
        else:
            if current.left:
                frontier.append((current.left, height + 1))
            if current.right:
                frontier.append((current.right, height + 1))

    return True

a = binary_tree_node.BinaryTreeNode(1)
b = binary_tree_node.BinaryTreeNode(2)
c = binary_tree_node.BinaryTreeNode(3)
d = binary_tree_node.BinaryTreeNode(4)
e = binary_tree_node.BinaryTreeNode(5)
a.left = b
b.left = c
c.left = d
a.right = e

print is_superbalanced(a) # False
