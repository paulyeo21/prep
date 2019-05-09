# Given a binary search tree, find the second largest element.

import binary_tree_node

def largest_in_bst(root):
    current = root
    while current:
        if current.right:
            current = current.right
        else:
            return current.value

def second_largest_in_bst(root):
    # Naive method would be to do an inorder traversal
    # and return the second to last element. T: O(n), S: O(h).

    # To find largest element is to go to the right most
    # node in the bst. 

    # To find the second largest at each node we need to check
    # 1) if we have a left subtree but not a right subtree, 
    # then the current node is the largest and return the largest
    # of the left subtree for the second largest. 2) if we have a
    # right child but not any children of that child, then the
    # right child is the largest so return current node. 3) else
    # we have a right subtree with more than one element so proceed.
    # T: O(h), S: O(1).

    current = root
    while current:
        if not current.right and current.left:
            return largest_in_bst(current.left)
        elif current.right and not current.right.right \
                and not current.right.left:
            return current.value
        else:
            current = current.right

a = binary_tree_node.BinaryTreeNode(2)
b = binary_tree_node.BinaryTreeNode(1)
a.left = b

print second_largest_in_bst(a) # 1

a = binary_tree_node.BinaryTreeNode(1)
b = binary_tree_node.BinaryTreeNode(2)
a.right = b

print second_largest_in_bst(a) # 1

a = binary_tree_node.BinaryTreeNode(1)
b = binary_tree_node.BinaryTreeNode(3)
c = binary_tree_node.BinaryTreeNode(2)
a.right = b
b.left = c

print second_largest_in_bst(a) # 2
