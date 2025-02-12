# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize maxDiameter in the outer scope so that the DFS function can update it.
        self.maxDiameter = 0

        # Define the DFS function which returns the height of the subtree rooted at 'node'.
        # We use the nonlocal keyword to modify maxDiameter from the outer scope.
        def dfs(node):
            
            # Base case: If the node is None, its height is -1.
            # This makes a leaf node have height 0 (since max(-1, -1) + 1 = 0).
            if node is None:
                return -1

            # Recursively compute the height of the left subtree.
            left_height = dfs(node.left)
            # Recursively compute the height of the right subtree.
            right_height = dfs(node.right)
            
            # The diameter passing through this node is the sum of left and right heights plus 2,
            # which represents the number of edges connecting the left and right subtrees through this node.
            self.maxDiameter = max(self.maxDiameter, left_height + right_height + 2)
            
            # Return the height of this node, which is the greater of the two subtree heights plus 1.
            return max(left_height, right_height) + 1

        # Start the DFS traversal from the root.
        dfs(root)
        # After the traversal, maxDiameter contains the longest path (in terms of number of edges).
        return self.maxDiameter

        
# 543. Diameter of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.9M
# Submissions
# 3M
# Acceptance Rate
# 62.6%
# Topics
# Tree
# Depth-First Search
# Binary Tree
# Companies
# 0 - 3 months
# Meta
# 57
# Google
# 4
# Amazon
# 4
# Bloomberg
# 2
# 0 - 6 months
# TikTok
# 2
# Visa
# 2
# 6 months ago
# Microsoft
# 14
# Apple
# 10
# Adobe
# 6
# Uber
# 4
# LinkedIn
# 3
# Oracle
# 3
# tcs
# 2
# Wix
# 2
# Yahoo
# 2
# Similar Questions
# Diameter of N-Ary Tree
# Medium
# Longest Path With Different Adjacent Characters
# Hard
# Discussion (287)