# Given a binary tree, check if it is a binary
# search tree. 

import binary_tree_node

def is_binary_search_tree(root):
    # Not bst if left child is greater than parent
    # or right child is less than parent.
    # While traversing tree, track max and min.
    # For instance, a node that is a right child of a left
    # child of a root, the node must be greater than
    # immediate parent but less than root value.
    # T: O(n)
    # S: O(n)

    # 1. DFS, because saves space
    # 2. Track floor and ceiling values
    # 3. Check if current node is in between
    #    floor and ceiling, otherwise False.

    frontier = [(root, -2**31, 2**32-1)]
    while len(frontier) > 0:
        current, floor, ceiling = frontier.pop()

        if current.value <= floor or \
                current.value >= ceiling:
            return False
        else:
            if current.left:
                frontier.append((current.left, floor, current.value))
            if current.right:
                frontier.append((current.right, current.value, ceiling))
    return True

# Recursive
def is_binary_search_tree(root, lower_bound=-2**31, upper_bound=2**32-1):
    if not root:
        return True

    if root.value >= upper_bound or root.value <= lower_bound:
        return False

    return is_binary_search_tree(root.left, lower_bound, root.value) \
            and is_binary_search_tree(root.right, root.value, upper_bound)

# Inorder traversal check
def is_sorted(ints):
    prev = ints[0]
    for i in xrange(1, len(ints)):
        if ints[i] < prev:
            return False
        prev = ints[i]
    return True

def is_binary_search_tree(root):
    inorder_traversal = is_binary_search_tree_helper(root, [])
    return is_sorted(inorder_traversal)

def is_binary_search_tree_helper(node, inorder_traversal_nodes):
    if not node:
        return inorder_traversal_nodes
    else:
        is_binary_search_tree_helper(node.left, inorder_traversal_nodes)
        inorder_traversal_nodes.append(node.value)
        return is_binary_search_tree_helper(node.right, inorder_traversal_nodes)

a = binary_tree_node.BinaryTreeNode(3)
b = binary_tree_node.BinaryTreeNode(1)
c = binary_tree_node.BinaryTreeNode(2)
a.left = b
b.right = c

print is_binary_search_tree(a) # True

a = binary_tree_node.BinaryTreeNode(2)
b = binary_tree_node.BinaryTreeNode(1)
c = binary_tree_node.BinaryTreeNode(3)
a.left = b
b.right = c

print is_binary_search_tree(a) # False
