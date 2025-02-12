#Method 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        def dfs(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root

        




# method 2
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        queue = deque([root])
        while queue:
            node=queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        

# 226. Invert Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.5M
# Submissions
# 3.1M
# Acceptance Rate
# 78.5%
# Topics
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
# Companies
# 0 - 3 months
# Google
# 5
# Amazon
# 2
# Oracle
# 2
# 0 - 6 months
# Bloomberg
# 4
# 6 months ago
# Microsoft
# 8
# Meta
# 7
# Apple
# 5
# Yahoo
# 5
# TikTok
# 3
# Adobe
# 2
# Ozon
# 2
# Similar Questions
# Reverse Odd Levels of Binary Tree
# Medium
# Discussion (169)