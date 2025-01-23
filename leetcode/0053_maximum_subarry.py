class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current=nums[0]
        max_global=nums[0]
        for i in range(1, len(nums)):
            max_current=max(nums[i], max_current+nums[i])
            if max_current>max_global:
                max_global=max_current
        return max_global
    

# 53. Maximum Subarray
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.6M
# Submissions
# 8.9M
# Acceptance Rate
# 51.6%
# Topics
# Array
# Divide and Conquer
# Dynamic Programming
# Companies
# 0 - 3 months
# Google
# 21
# Amazon
# 12
# Meta
# 9
# Microsoft
# 9
# LinkedIn
# 5
# Bloomberg
# 4
# Cisco
# 4
# Accenture
# 3
# Upstart
# 3
# 0 - 6 months
# Apple
# 4
# Oracle
# 3
# Goldman Sachs
# 3
# Uber
# 3
# PayPal
# 3
# Infosys
# 2
# TikTok
# 2
# Nike
# 2
# Cognizant
# 2
# SAP
# 2
# 6 months ago
# Adobe
# 23
# tcs
# 14
# Yahoo
# 8
# Walmart Labs
# 5
# J.P. Morgan
# 4
# Zoho
# 4
# DE Shaw
# 3
# Samsung
# 3
# ServiceNow
# 3
# Salesforce
# 3
# Similar Questions
# Best Time to Buy and Sell Stock
# Easy
# Maximum Product Subarray
# Medium
# Degree of an Array
# Easy
# Longest Turbulent Subarray
# Medium
# Maximum Score Of Spliced Array
# Hard
# Maximum Absolute Sum of Any Subarray
# Medium
# Maximum Subarray Sum After One Operation
# Medium
# Substring With Largest Variance
# Hard
# Count Subarrays With Score Less Than K
# Hard
# Maximum Value of a String in an Array
# Easy
# Find the Substring With Maximum Cost
# Medium
# K Items With the Maximum Sum
# Easy
# Maximum Good Subarray Sum
# Medium
# Maximize Subarray Sum After Removing All Occurrences of One Element
# Hard
# Discussion (313)