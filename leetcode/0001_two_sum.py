class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i
        return []


# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 15.8M
# Submissions
# 29M
# Acceptance Rate
# 54.7%
# Topics
# Array
# Hash Table
# Companies
# 0 - 3 months
# Google
# 181
# Amazon
# 73
# Meta
# 49
# Microsoft
# 48
# Bloomberg
# 24
# Apple
# 9
# Oracle
# 6
# Goldman Sachs
# 4
# Visa
# 4
# Infosys
# 3
# 0 - 6 months
# tcs
# 11
# Yandex
# 8
# Walmart Labs
# 6
# Adobe
# 5
# Accenture
# 5
# Salesforce
# 5
# IBM
# 4
# TikTok
# 4
# Uber
# 4
# Nvidia
# 4
# 6 months ago
# Yahoo
# 88
# Capgemini
# 12
# Deloitte
# 10
# Zoho
# 10
# Wipro
# 10
# SAP
# 9
# Spotify
# 8
# Tinkoff
# 7
# Cisco
# 7
# Morgan Stanley
# 6
# Hint 1
# A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.
# Hint 2
# So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
# Hint 3
# The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
# Similar Questions
# 3Sum
# Medium
# 4Sum
# Medium
# Two Sum II - Input Array Is Sorted
# Medium
# Two Sum III - Data structure design
# Easy
# Subarray Sum Equals K
# Medium
# Two Sum IV - Input is a BST
# Easy
# Two Sum Less Than K
# Easy
# Max Number of K-Sum Pairs
# Medium
# Count Good Meals
# Medium
# Count Number of Pairs With Absolute Difference K
# Easy
# Number of Pairs of Strings With Concatenation Equal to Target
# Medium
# Find All K-Distant Indices in an Array
# Easy
# First Letter to Appear Twice
# Easy
# Number of Excellent Pairs
# Hard
# Number of Arithmetic Triplets
# Easy
# Node With Highest Edge Score
# Medium
# Check Distances Between Same Letters
# Easy
# Find Subarrays With Equal Sum
# Easy
# Largest Positive Integer That Exists With Its Negative
# Easy
# Number of Distinct Averages
# Easy
# Count Pairs Whose Sum is Less than Target
# Easy
# Discussion (1.2K)
