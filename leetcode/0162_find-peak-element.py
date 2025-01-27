class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        res = 0
        while low < high:
            mid = (low + high) // 2
            res = mid
            if nums[mid] > nums[mid + 1]:
                high = mid
                res = high
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
                res = low
        return res


# 162. Find Peak Element
# Solved
# Medium
# Topics
# Companies
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.7M
# Submissions
# 3.8M
# Acceptance Rate
# 46.3%
# Topics
# Array
# Binary Search
# Companies
# 0 - 3 months
# Meta
# 78
# Google
# 17
# Amazon
# 7
# Bloomberg
# 6
# Microsoft
# 2
# Goldman Sachs
# 2
# 0 - 6 months
# TikTok
# 3
# Uber
# 3
# Zepto
# 3
# IXL
# 3
# Wix
# 2
# Accenture
# 2
# PayPal
# 2
# Commvault
# 2
# 6 months ago
# Adobe
# 19
# Apple
# 19
# Oracle
# 3
# Yahoo
# 3
# tcs
# 2
# Flipkart
# 2
# Zoho
# 2
# Nvidia
# 2
# Snap
# 2
# Similar Questions
# Peak Index in a Mountain Array
# Medium
# Find a Peak Element II
# Medium
# Pour Water Between Buckets to Make Water Levels Equal
# Medium
# Count Hills and Valleys in an Array
# Easy
# Find the Peaks
# Easy
# Discussion (296)