# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the node is None, its depth is 0; otherwise, return 1 (for the current node)
        # plus the maximum depth of its left and right subtrees.
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.7M
# Submissions
# 4.9M
# Acceptance Rate
# 76.7%
# Topics
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
# Companies
# 0 - 3 months
# Amazon
# 4
# Microsoft
# 2
# Arista Networks
# 2
# 0 - 6 months
# Meta
# 5
# Google
# 4
# Bloomberg
# 2
# LinkedIn
# 2
# 6 months ago
# Yahoo
# 10
# Adobe
# 8
# Apple
# 8
# Uber
# 6
# Yandex
# 3
# SAP
# 3
# Accenture
# 2
# Turing
# 2
# Similar Questions
# Balanced Binary Tree
# Easy
# Minimum Depth of Binary Tree
# Easy
# Maximum Depth of N-ary Tree
# Easy
# Time Needed to Inform All Employees
# Medium
# Amount of Time for Binary Tree to Be Infected
# Medium
# Height of Binary Tree After Subtree Removal Queries
# Hard
# Discussion (155)