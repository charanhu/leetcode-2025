class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        res.append(nums[0])
        for i in range(1, n):
            res.append(nums[i]+res[i-1])
        return res
        
    

#     1480. Running Sum of 1d Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2M
# Submissions
# 2.3M
# Acceptance Rate
# 86.9%
# Topics
# Array
# Prefix Sum
# Companies
# 0 - 3 months
# Google
# 4
# tcs
# 2
# 0 - 6 months
# Amazon
# 4
# 6 months ago
# Adobe
# 16
# Microsoft
# 11
# Apple
# 11
# Bloomberg
# 10
# Meta
# 3
# Uber
# 3
# Accenture
# 2
# Yahoo
# 2
# Hint 1
# Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.