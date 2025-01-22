class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = list(map(lambda a: a*a, nums))
        nums.sort()
        return nums

        
# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.1M
# Submissions
# 2.8M
# Acceptance Rate
# 73.0%
# Topics
# Array
# Two Pointers
# Sorting
# Companies
# 0 - 3 months
# Meta
# 8
# Uber
# 7
# Google
# 2
# Bloomberg
# 2
# Yandex
# 2
# 0 - 6 months
# Amazon
# 6
# Agoda
# 2
# Instacart
# 2
# 6 months ago
# Apple
# 9
# Adobe
# 5
# Walmart Labs
# 5
# Yahoo
# 5
# Microsoft
# 4
# Ozon
# 4
# Tinkoff
# 3
# tcs
# 2
# Oracle
# 2
# Similar Questions
# Merge Sorted Array
# Easy
# Sort Transformed Array
# Medium
# Discussion (119)