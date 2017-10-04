# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.val += t2.val
        return t1

t1_1 = TreeNode(1)
t1_3 = TreeNode(3)
t1_2 = TreeNode(2)
t1_5 = TreeNode(5)
t1_1.left = t1_3
t1_1.right = t1_2
t1_3.left = t1_5

t2_2 = TreeNode(2)
t2_1 = TreeNode(1)
t2_3 = TreeNode(3)
t2_4 = TreeNode(4)
t2_7 = TreeNode(7)
t2_2.left = t2_1
t2_2.right = t2_3
t2_1.right = t2_4
t2_3.right = t2_7

s = Solution()
merged_tree = s.mergeTrees(t1_1, t2_2)

# BFS
queue = []
queue.append(merged_tree)
while len(queue) != 0:
    current = queue.pop(0)
    print current.val
    if current.left:
        queue.append(current.left)
    if current.right:
        queue.append(current.right)

