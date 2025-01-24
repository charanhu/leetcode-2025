class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        coverage = [0] * n
        
        # Mark the start and end of each query range
        for l, r in queries:
            coverage[l] += 1
            if r + 1 < n:
                coverage[r + 1] -= 1
        
        total_decrements = 0
        for i in range(n):
            total_decrements += coverage[i]
            if total_decrements < nums[i]:
                return False  # Early termination upon failure
        
        return True  # All indices satisfy the condition
    

# 3355. Zero Array Transformation I
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

# For each queries[i]:

# Select a 
# subset
#  of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.

# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

 

# Example 1:

# Input: nums = [1,0,1], queries = [[0,2]]

# Output: true

# Explanation:

# For i = 0:
# Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
# The array will become [0, 0, 0], which is a Zero Array.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

# Output: false

# Explanation:

# For i = 0:
# Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
# The array will become [4, 2, 1, 0].
# For i = 1:
# Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
# The array will become [3, 1, 0, 0], which is not a Zero Array.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= li <= ri < nums.length
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 26.6K
# Submissions
# 63.7K
# Acceptance Rate
# 41.8%
# Topics
# Array
# Prefix Sum
# Companies
# 0 - 3 months
# Google
# 35
# Hint 1
# Can we use difference array and prefix sum to check if an index can be made zero?
# Discussion (30)
