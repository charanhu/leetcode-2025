class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n <= 0:
            return
        if n<2:
            return True
        for i in range(n-1):
            if nums[i]%2 == nums[i+1]%2:
                return False
        return True





#     3151. Special Array I
# Solved
# Easy
# Topics
# Companies
# Hint
# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

# Example 1:

# Input: nums = [1]

# Output: true

# Explanation:

# There is only one element. So the answer is true.

# Example 2:

# Input: nums = [2,1,4]

# Output: true

# Explanation:

# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

# Example 3:

# Input: nums = [4,3,1,6]

# Output: false

# Explanation:

# nums[1] and nums[2] are both odd. So the answer is false.

 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 202.1K
# Submissions
# 246K
# Acceptance Rate
# 82.2%
# Topics
# Array
# Companies
# 0 - 3 months
# Google
# 7
# Microsoft
# 4
# 6 months ago
# Amazon
# 3
# National Payments Corporation of India
# 2
# Hint 1
# Try to check the parity of each element and its previous element.
# Discussion (201)