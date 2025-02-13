# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both nodes are None, there is nothing to merge, so return None.
        if not root1 and not root2:
            return root1  # Could also return None here.
        
        # If root1 is None but root2 is not, then the merged tree should be root2.
        if not root1 and root2:
            return root2
        
        # If root1 exists but root2 is None, then the merged tree should be root1.
        if root1 and not root2:
            return root1
        
        # At this point, both root1 and root2 are not None.
        # Merge the values from both nodes by summing them.
        root1.val = root1.val + root2.val
        
        # Recursively merge the left children of both nodes.
        root1.left = self.mergeTrees(root1.left, root2.left)
        
        # Recursively merge the right children of both nodes.
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        # Return the merged tree rooted at root1.
        return root1



# 617. Merge Two Binary Trees
# Solved
# Easy
# Topics
# Companies
# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

 

# Example 1:


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:

# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
 

# Constraints:

# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 821K
# Submissions
# 1M
# Acceptance Rate
# 79.3%
# Topics
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree
# Companies
# 0 - 3 months
# Amazon
# 2
# Bloomberg
# 2
# 0 - 6 months
# Google
# 2
# Meta
# 2
# MongoDB
# 2
# 6 months ago
# Apple
# 3
# Adobe
# 2
# Uber
# 2
# Yahoo
# 2
# Discussion (31)