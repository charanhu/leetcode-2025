class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones=0
        count=0
        for num in nums:
            if num==1:
                count+=1
            else:
                count=0
            max_ones=max(max_ones, count)
        return max_ones
            

        


# 485. Max Consecutive Ones
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.5M
# Submissions
# 2.5M
# Acceptance Rate
# 61.6%
# Topics
# Array
# Companies
# 0 - 3 months
# Google
# 13
# Meta
# 4
# Amazon
# 3
# Microsoft
# 2
# Bloomberg
# 2
# 0 - 6 months
# Accenture
# 2
# Yandex
# 2
# 6 months ago
# Adobe
# 6
# Uber
# 4
# Apple
# 3
# tcs
# 2
# Oracle
# 2
# Hint 1
# You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
# Similar Questions
# Max Consecutive Ones II
# Medium
# Max Consecutive Ones III
# Medium
# Consecutive Characters
# Easy
# Longer Contiguous Segments of Ones than Zeros
# Easy
# Length of the Longest Alphabetical Continuous Substring
# Medium
# Maximum Enemy Forts That Can Be Captured
# Easy
# Discussion (66)