class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(queries)
        left, right = 0, m  # Initialize search range including k=0
        result = -1

        while left <= right:
            mid = (left + right) // 2

            # Initialize Difference Array
            diff = [0] * (n + 1)

            # Apply first 'mid' queries
            for i in range(mid):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v

            # Compute Prefix Sum to get coverage
            current = 0
            feasible = True
            for i in range(n):
                current += diff[i]
                if current < nums[i]:
                    feasible = False
                    break

            if feasible:
                result = mid
                right = mid - 1  # Try to find a smaller k
            else:
                left = mid + 1  # Need more queries

        return result
    

# 3356. Zero Array Transformation II
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

# Example 1:

# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

# Output: 2

# Explanation:

# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

# Output: -1

# Explanation:

# For i = 0 (l = 1, r = 3, val = 2):
# Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
# The array will become [4, 1, 0, 0].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
# The array will become [3, 0, 0, 0], which is not a Zero Array.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 5 * 105
# 1 <= queries.length <= 105
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 17.1K
# Submissions
# 46.1K
# Acceptance Rate
# 37.0%
# Topics
# Array
# Binary Search
# Prefix Sum
# Companies
# 0 - 3 months
# Google
# 21
# Hint 1
# Can we apply binary search here?
# Hint 2
# Utilize a difference array to optimize the processing of queries.
# Similar Questions
# Corporate Flight Bookings
# Medium
# Minimum Moves to Make Array Complementary
# Medium
# Discussion (28)
