# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = []
        to_delete_set = set(to_delete)

        def dfs(node, has_parent):
            if not node:
                return None
            delete_current = node.val in to_delete_set
            if not delete_current and not has_parent:
                result.append(node)
            node.left = dfs(node.left, not delete_current)
            node.right = dfs(node.right, not delete_current)
            return None if delete_current else node

        dfs(root, False)
        return result
    

# 1110. Delete Nodes And Return Forest
# Solved
# Medium
# Topics
# Companies
# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
 

# Constraints:

# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 357.9K
# Submissions
# 493.8K
# Acceptance Rate
# 72.5%
# Topics
# Array
# Hash Table
# Tree
# Depth-First Search
# Binary Tree
# Companies
# 0 - 3 months
# Google
# 3
# Meta
# 2
# 6 months ago
# Amazon
# 4
# TikTok
# 2
# Similar Questions
# Count Nodes With the Highest Score