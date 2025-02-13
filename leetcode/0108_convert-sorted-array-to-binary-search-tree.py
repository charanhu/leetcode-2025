# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base Case: If the input list is empty, return None.
        if not nums:
            return None
        
        # Find the middle index of the current list.
        mid = len(nums) // 2
        
        # Create a new TreeNode with the middle element as the value.
        # This will be the root of the BST (or subtree).
        root = TreeNode(nums[mid])
        
        # Recursively construct the left subtree using the left half of the list.
        # The left half contains all elements to the left of the middle element.
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively construct the right subtree using the right half of the list.
        # The right half contains all elements to the right of the middle element.
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        # Return the root of the BST.
        return root

# 108. Convert Sorted Array to Binary Search Tree
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.4M
# Submissions
# 1.9M
# Acceptance Rate
# 73.4%
# Topics
# Array
# Divide and Conquer
# Tree
# Binary Search Tree
# Binary Tree
# Companies
# 0 - 3 months
# Google
# 4
# Amazon
# 4
# 0 - 6 months
# Meta
# 3
# Microsoft
# 3
# Bloomberg
# 2
# 6 months ago
# Apple
# 5
# Adobe
# 4
# Airbnb
# 2
# Samsung
# 2
# Similar Questions
# Convert Sorted List to Binary Search Tree
# Medium
# Discussion (119)