# 10. Given a list of words that are alphabetically ordered but rotated, find rotation point.

# Clarifications:
#   a) Given an array of strings that were in order, but now some are out of order, because
#      the words have been rotated, return the index of the first string in the original order.
#   b) For example, if ['e','a','b','c','d'] -> the rotation point is index at 1.
#   c) Will rotation point always exist? Yes.
#   d) Can we be given an empty array? No.
#   e) Can we be given any Nones? No.
#   f) Can we given a not rotated input? Yes.
# Edge cases:
#   a) Given ['a','b','c'] return 0
#   b) Given ['b','c','a'] return 2
#   c) Given ['a'] return 0
#   d) Given ['ax','ay','az','aa','ab','ac'] return 3
# Algorithms:
#   a) We are going to use binary search to find which half of the input list to find the rotation
#      point. Comparing the element at the mid index versus the first element and the last element,
#      we know that if the mid element is greater than the first element, then the first half of the
#      list is in order (unless we were given an in-ordered list, then we want to return 0), similarly,
#      if the last element is greater than the mid element, then we know that the second half of the list
#      is in order. Using this when it is not in order we take that half and continue this algorithm
#      until we find the rotation point. T: O(lg n) S: O(1)

def findRotationPoint(strings, left, right):
    if len(strings) == 1:
        return 0

    while left <= right:
        mid = (left + right) / 2

        # if current mid is the rotation point
        if strings[mid] < strings[mid-1]:
            return mid

        if strings[left] > strings[mid]:
            right = mid - 1
        elif strings[right] < strings[mid]:
            left = mid + 1
        else:
            # if order is preserved
            return left

assert(findRotationPoint(['a'], 0, 1) == 0)
assert(findRotationPoint(['a','b','c'], 0, 2) == 0)
assert(findRotationPoint(['b','c','a'], 0, 2) == 2)
assert(findRotationPoint(['ax','ay','az','aa','ab','ac'], 0, 5) == 3)

# 11. Implement iterative BFS, DFS, Dijkstra's, Greedy Best First Search, and A* and explain why
#     you would use one over the other.
#
# Clarifications:
#   a) BFS is Breadth First Search, DFS is Depth First Search, Dijkstra's is implemented with a
#      cost heuristic that makes decisions based on the total cost to make a move. Greedy Best
#      First Search makes decisions based on the shortest distance to the end goal. A* is a combination
#      of total cost and distance to goal.
# Algorithms:
#   a) The Big-O time complexities for BFS and DFS are the same except BFS will on average use more
#      space than DFS. T: O(V + E) S: O(V).
#   b) You would want to use BFS or DFS for graph traversals where cost is not part of the equation. Use
#      Dijkstra's when there are costs involved and you want to find paths from or to all locations. Use
#      Greedy Best First Search when you want to find the shortest path to one location. Use A* is guaranteed
#      to find the best shortest path, while Greedy Best First Search is not. 

from collections import deque

def bfs(start):
    frontier = deque([start])
    traversed = []
    while len(frontier) != 0:
        current = frontier.popleft()
        traversed.append(current)
        for neighbor in current.neighbors:
            frontier.append(neighbor)
    return traversed

def dfs(start):
    frontier = [start]
    traversed = []
    while len(frontier) != 0:
        current = frontier.pop()
        traversed.append(current)
        for neighbor in current.neighbors:
            frontier.append(neighbor)
    return traversed

def dijkstras(start):
    frontier = [(start, 0)] # priority queue
    cost_so_far = {}
    while len(frontier) != 0:
        current, cost = frontier.pop()
        total_cost = cost + cost_so_far[current]

        for neighbor in current.neighbors:
            if neighbor not in cost_so_far or cost_so_far[neighbor] > total_cost:
                total_cost = cost + cost_so_far[current]
                cost_so_far[neighbor] = total_cost
                frontier.append((neighbor, total_cost))

def gfs(start, end):
    frontier = [] # priority queue
    came_from = {}
    while len(frontier) != 0:
        current = frontier.pop()
        for neighbor in current.neighbors:
            if neighbor not in came_from:
                frontier.append(distance(neighbor, end))
                came_from[neighbor] = current

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node3]
node2.neighbors = [node4]
# print(bfs(node1))
# print(dfs(node1))

# 12. Given an undirected graph with maximum degree D, find a graph coloring using at most
#     D + 1 colors.
#
# Clarifications:
#   a) Given nodes with at most D number of connections, color the different nodes with
#      no neighbors with same colors. 
#   b) Is this always possible? Yes.
#   c) Can there be loops? No.
#   d) Can there be nodes with no edges? No.
#   e) Can there be cycles? Yes.
# Edge cases:
#   a) Given graph with one node, zero edges, return one color.
#   b) Given graph with three nodes, three edges, return each node with different colors.

def colorGraph(graph, colors):
    frontier = [graph]
    visited = set()
    while len(frontier) != 0:
        current = frontier.pop()
        visited.add(current)
        illegal_colors = set([
            neighbor.color
            for neighbor in current.neighbors
            if neighbor.color
        ])
        for color in colors:
            if color not in illegal_colors:
                current.color = color
                break
        for neighbor in current.neighbors:
            if neighbor not in visited:
                frontier.append(neighbor)

def confirmGraphColoring(graph):
    frontier = [graph]
    visited = set()
    while len(frontier) != 0:
        current = frontier.pop()
        visited.add(current)
        previous_color = current.color
        if not previous_color:
            return False

        for neighbor in current.neighbors:
            if neighbor not in visited:
                if neighbor.color == previous_color:
                    return False
                frontier.append(neighbor)
    return True

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return str(self.label)

node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node2.neighbors.add(node3)
node2.neighbors.add(node4)
node3.neighbors.add(node2)
node3.neighbors.add(node4)
node4.neighbors.add(node2)
node4.neighbors.add(node3)
colors1 = ['red']
colors2 = ['red','blue','green','yellow']

colorGraph(node1, colors1)
assert(confirmGraphColoring(node1) == True)
colorGraph(node2, colors2)
assert(confirmGraphColoring(node2) == True)

# 13. Implement inorder, postorder, and preorder traversals
#
# Clarifications:
#   a) Inorder traversal is left, root, right. Postorder is left, 
#      right, root. Preorder is root, left, right.

def inorder(graph):
    if graph:
        inorder(graph.left)
        print(graph.label)
        inorder(graph.right)

def postorder(graph):
    if graph:
        postorder(graph.left)
        postorder(graph.right)
        print(graph.label)

def preorder(graph):
    if graph:
        print(graph.label)
        preorder(graph.left)
        preorder(graph.right)

class BinaryNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

node1 = BinaryNode(1)
node2 = BinaryNode(2)
node3 = BinaryNode(3)
node4 = BinaryNode(4)
node5 = BinaryNode(5)
node1.left = node2
node2.right = node3
node2.left = node4
node2.right = node5

# inorder(node1)
# postorder(node1)
# preorder(node1)

# 14. Check if a binary tree is superbalanced, meaning difference
#     in height of leaves is < 2. 
#
# Edge cases:
#   a) Given a single node, return True.
#   b) Given a left only three node tree, return True.
#   c) Given a left subree thats height 3 and right subtree with
#      height 1, return False.
#
# Algorithms:
#   a) We traverse the tree and when we hit a leaf node, we note the
#      height. If we have more than 2 distinct heights, then we know
#      that the tree is not superbalanced, so return False. Otherwise
#      True.

def isSuperBalanced(root):
    dfs = [(root, 0)]
    heights = []

    while len(dfs) != 0:
        current, height = dfs.pop()

        if current.left:
            dfs.append((current.left, height + 1))

        if current.right:
            dfs.append((current.right, height + 1))

        if not current.left and not current.right:
            if height not in heights:
                heights.append(height)

                if len(heights) > 2:
                    return False
                if len(heights) == 2 and abs(heights[0] - heights[1]) > 1:
                    return False
    return True

tree1 = BinaryNode(1)
tree2 = BinaryNode(1)
tree2_node2 = BinaryNode(2)
tree2_node3 = BinaryNode(3)
tree2.left = tree2_node2
tree2_node2.left = tree2_node3
tree3 = BinaryNode(1)
tree3_node2 = BinaryNode(2)
tree3_node3 = BinaryNode(3)
tree3_node4 = BinaryNode(4)
tree3_node5 = BinaryNode(5)
tree3.left = tree3_node2
tree3_node2.left = tree3_node3
tree3_node3.left = tree3_node4
tree3.right = tree3_node5

assert(isSuperBalanced(tree1) == True)
assert(isSuperBalanced(tree2) == True)
assert(isSuperBalanced(tree3) == False)

# 15. Find the second largest element in a binary search tree.
#
# Clarifications:
#   a) Can we be given a tree with one node? No.
#
# Edge cases:
#   a) Tree with no right subtree should return the largest element in left subtree.
#   b) Tree with right subree but not left subtree should return parent node of right most node.
#
# Algorithms:
#   a) At current node, check if right exists, if it does check if right right exists.
#      If right right exists, then restart algo as right node. If right right does not exist,
#      check if right left exists. If right left does not exist, return current node value.
#      If right left exists, return the greatest value of right left subtree. T: O(n) S: O(1)

def largestInBST(root):
    if root.right:
        return largestInBST(root.right)

    return root.label

def secondLargestInBST(root):
    if root.right:
        if root.right.right:
            return secondLargestInBST(root.right)
        else:
            if root.right.left:
                return largestInBST(root.right.left)
            else:
                return root.label

    return largestInBST(root.left)

bst1 = BinaryNode(2)
bst1.left = BinaryNode(1)

bst2 = BinaryNode(4)
bst2_node2 = BinaryNode(5)
bst2_node3 = BinaryNode(6)
bst2_node4 = BinaryNode(7)
bst2_node5 = BinaryNode(8)
bst2.right = bst2_node5
bst2_node5.left = bst2_node2
bst2_node2.right = bst2_node3
bst2_node3.right = bst2_node4

bst3 = BinaryNode(3)
bst3_node2 = BinaryNode(4)
bst3_node3 = BinaryNode(5)
bst3.right = bst3_node2
bst3_node2.right = bst3_node3

assert(secondLargestInBST(bst1) == 1)
assert(secondLargestInBST(bst2) == 7)
assert(secondLargestInBST(bst3) == 4)

# 16. Check if binary tree is a binary search tree.
#
# Clarifications:
#   a) Left subtree is less than parent, while right subtree is greater
#      than parent.
#   b) Can we be given a None? No.
#   c) Can we be given nodes with no values? No.
#   d) Are the node values integers? Yes.
#
# Edge cases:
#   a) Given a tree with a left subtree that has a right subtree, the right subtree
#      should be less than root value.
#   b) Similarly, a tree with a right subtree that has a left subtree, the left subtree
#      values should be greater than root.
#   c) Right subtree nodes should be greater than root.
#   d) Left subtree nodes should be less than root.
#
# Algorithms:
#   a) Traverse the tree (dfs) but tracking the max and min values at each node. For example,
#      at root, the max and min are 2**31-1 and -2**31, while if root value is 10, and there is
#      a left node, the max left node value is 10. T: O(v + e) S: O(e)

def isBST(root):
    dfs = [(root, 2**31-1, -2**31)]

    while len(dfs) != 0:
        current, maximum, minimum = dfs.pop()

        if current.label > maximum or current.label < minimum:
            return False

        if current.left:
            dfs.append((current.left, current.label, minimum))

        if current.right:
            dfs.append((current.right, maximum, current.label))

    return True

bst1 = BinaryNode(10)
bst1.left = BinaryNode(9)
bst2 = BinaryNode(1)
bst2.left = BinaryNode(2)
bst3 = BinaryNode(10)
bst3_node2 = BinaryNode(5)
bst3_node3 = BinaryNode(7)
bst3.left = bst3_node2
bst3_node2.right = bst3_node3
bst4 = BinaryNode(5)
bst4_node2 = BinaryNode(10)
bst4_node3 = BinaryNode(7)
bst4.right = bst4_node2
bst4_node2.left = bst4_node3
bst5 = BinaryNode(7)
bst5_node2 = BinaryNode(10)
bst5_node3 = BinaryNode(5)
bst5.right = bst5_node2
bst5_node2.left = bst5_node3

assert(isBST(bst1) == True)
assert(isBST(bst2) == False)
assert(isBST(bst3) == True)
assert(isBST(bst4) == True)
assert(isBST(bst5) == False)

# 17. Given a list of integers, for each index return the product of
#     every number except for the number at index without using division.
#
# Clarifications:
#   a) [1, 10, 3, 2] => [10 * 3 * 2, 1 * 3 * 2, 1 * 10 * 2, 1 * 10 * 3]
#   b) Can we be given 0? Yes.
#   c) Can we be given None? No.
#
# Edge cases:
#   a) [0, 1, 10] => [1, 0, 0]
#   b) [1, 2, 3] => [2 * 3, 1 * 3, 1 * 2]
#
# Algorithms:
#   a) Do two passes, the first pass will compute all numbers up to that index,
#      while the second pass goes backwards from n-1 index to 0 computing all
#      numbers up to that index as well, returning us the product except for
#      the number at index. For instance, given [1, 2, 3], initially we will have 
#      [1, 1, 1] and first pass we will have [1, 1 * 1, 1 * (1 * 1) * 2], and
#      second pass we would get [1 * 2 * (1 * 1 * 3), 1 * 1 * 3, 1 * (1 * 1) * 2].
#      T: O(n) S: O(n)

def productExceptAtIndex(integers):
    if not integers:
        return []

    output = [1] * len(integers)

    # first pass
    previous = integers[0]
    for i in range(1, len(integers)):
        output[i] *= previous
        previous *= integers[i]

    # second pass
    previous = integers[-1]
    for i in range(len(integers)-2, -1, -1):
        output[i] *= previous
        previous *= integers[i]

    return output

assert(productExceptAtIndex([]) == [])
assert(productExceptAtIndex([0, 1, 10]) == [10, 0, 0])
assert(productExceptAtIndex([1, 2, 3]) == [6, 3, 2])

# 18. Compute the nth fibonacci number. Compute using memoization. Compute using bottom-up.
#
# Clarifications:
#   a) Fibonacci is the sequence of the numbers starting with 0 and 1 where you add the previous two numbers.
#   b) Use memoization means there will be duplicate work so cache that work.
#   c) Bottom-up means to
