# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: if the node is None, there is no sum.
        if not root:
            return 0
        
        # If current node's value is less than low,
        # then the left subtree is guaranteed to have values < low.
        # Hence, we only explore the right subtree.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If current node's value is greater than high,
        # then the right subtree is guaranteed to have values > high.
        # So, we only explore the left subtree.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # Otherwise, current node's value is within [low, high].
        # We include its value and recursively sum both subtrees.
        return (root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high))
    

# METHOD 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        total=0
        def dfs(node):
            if not node:
                return 0
            nonlocal total
            if node.val>=low and node.val<=high:
                total+=node.val
            if node.val>=low:
                dfs(node.left)
            if node.val<=high:
                dfs(node.right)
            return total
        return dfs(root)
        



# 938. Range Sum of BST
# Solved
# Easy
# Topics
# Companies
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 1.4M
# Acceptance Rate
# 87.3%
# Topics
# Tree
# Depth-First Search
# Binary Search Tree
# Binary Tree
# Companies
# 0 - 3 months
# Meta
# 49
# Google
# 3
# 0 - 6 months
# Microsoft
# 2
# Yandex
# 2
# 6 months ago
# Amazon
# 7
# Apple
# 3
# Adobe
# 2
# Yahoo
# 2
# Discussion (147)