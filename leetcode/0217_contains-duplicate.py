class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # duplicates = {}
        # for num in nums:
        #     if num in duplicates:
        #         return True
        #         break
        #     duplicates[num] = 1
        # return False
        duplicates = set()
        for num in nums:
            if num in duplicates:
                return True
                break
            duplicates.add(num)
        return False
        




# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.8M
# Submissions
# 7.7M
# Acceptance Rate
# 62.8%
# Topics
# Array
# Hash Table
# Sorting
# Companies
# 0 - 3 months
# Google
# 6
# Amazon
# 6
# Bloomberg
# 5
# Meta
# 3
# 0 - 6 months
# Microsoft
# 5
# Zoho
# 2
# Paycom
# 2
# 6 months ago
# Apple
# 26
# Adobe
# 20
# Uber
# 16
# Yahoo
# 16
# tcs
# 4
# Yandex
# 3
# J.P. Morgan
# 2
# Oracle
# 2
# EPAM Systems
# 2
# DE Shaw
# 2
# Similar Questions
# Contains Duplicate II
# Easy
# Contains Duplicate III
# Hard
# Make Array Zero by Subtracting Equal Amounts
# Easy
# Find Valid Pair of Adjacent Digits in String
# Easy
# Discussion (336)