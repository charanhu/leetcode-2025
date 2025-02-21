# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                if node1.val!=node2.val:
                    return False
                if node1.val==node2.val:
                    return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            return False
        return dfs(p, q)

        


# 100. Same Tree
# Solved
# Easy
# Topics
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.6M
# Submissions
# 4.1M
# Acceptance Rate
# 64.4%
# Topics
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
# Companies
# Discussion (189)