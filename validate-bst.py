"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3
Binary tree [2,1,3], return true.

Example 2:

    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""

# T: O(V)
# S: O(1)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    def isValidBST(self, root, debug=False):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTUtil(root, float("-inf"), float("inf"))

    def isValidBSTUtil(self, root, minimum, maximum):
        # print root, minimum, maximum
        if not root: # If leaf
            return True
        if root.val >= maximum or root.val <= minimum:
            return False
        return self.isValidBSTUtil(root.left, minimum, root.val) and \
                self.isValidBSTUtil(root.right, root.val, maximum)

s = Solution()

def testcase1():
    one = TreeNode(1)
    assert s.isValidBST(one) == True

def testcase2():
    two = TreeNode(2)
    two1 = TreeNode(2)
    two.left = two1
    assert s.isValidBST(two) == False

def testcase3():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    two.left = one
    two.right = three
    assert s.isValidBST(two) == True

def testcase4():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    one.left = two
    one.right = three
    assert s.isValidBST(one) == False

def testcase5():
    ten = TreeNode(10)
    five = TreeNode(5)
    fifteen = TreeNode(15)
    six = TreeNode(6)
    twenty = TreeNode(20)
    ten.left = five
    ten.right = fifteen
    fifteen.left = six
    fifteen.right = twenty
    assert s.isValidBST(ten) == False

testcase1()
testcase2()
testcase3()
testcase4()
testcase5()

