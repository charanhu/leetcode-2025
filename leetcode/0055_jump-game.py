class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n: total number of positions in the nums array.
        n = len(nums)
        
        # maxJump: the farthest index that can be reached so far.
        maxJump = 0
        
        # Iterate over every index in the array.
        for i in range(n):
            # If the current index i is greater than the farthest reachable index,
            # it means we cannot reach this position. Hence, return False.
            if i > maxJump:
                return False
            
            # Update maxJump to be the maximum of its current value and
            # the index i plus the jump length from position i (i + nums[i]).
            maxJump = max(maxJump, i + nums[i])
        
        # After processing all indices, if maxJump is greater than or equal to the last index (n-1),
        # it means we can reach or surpass the last index. Hence, return True.
        return maxJump >= n - 1




# 55. Jump Game
# Solved
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.4M
# Submissions
# 6.2M
# Acceptance Rate
# 39.1%
# Topics
# Array
# Dynamic Programming
# Greedy
# Companies
# 0 - 3 months
# Amazon
# 21
# Google
# 12
# Microsoft
# 6
# Bloomberg
# 3
# Oracle
# 2
# Shopee
# 2
# 0 - 6 months
# tcs
# 7
# Meta
# 6
# Apple
# 4
# Adobe
# 2
# TikTok
# 2
# Goldman Sachs
# 2
# Cisco
# 2
# TomTom
# 2
# 6 months ago
# Yahoo
# 12
# Uber
# 9
# DoorDash
# 7
# Salesforce
# 5
# Infosys
# 4
# Media.net
# 4
# MakeMyTrip
# 4
# Verily
# 4
# Morgan Stanley
# 3
# ZScaler
# 3
# Similar Questions
# Jump Game II
# Medium
# Jump Game III
# Medium
# Jump Game VII
# Medium
# Jump Game VIII
# Medium
# Minimum Number of Visited Cells in a Grid
# Hard
# Largest Element in an Array after Merge Operations
# Medium
# Discussion (306)