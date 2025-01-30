class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum_counts = {}  # Initialize as empty
        current_sum = 0
        
        for num in nums:
            current_sum += num
            
            # Check if current_sum equals k
            if current_sum == k:
                count += 1
            
            # Check if (current_sum - k) exists in the hash map
            if (current_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]
            
            # Update the prefix_sum_counts dictionary
            if current_sum in prefix_sum_counts:
                prefix_sum_counts[current_sum] += 1
            else:
                prefix_sum_counts[current_sum] = 1
        
        return count

# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.6M
# Submissions
# 3.5M
# Acceptance Rate
# 44.7%
# Topics
# Array
# Hash Table
# Prefix Sum
# Companies
# Hint 1
# Will Brute force work here? Try to optimize it.
# Hint 2
# Can we optimize it by using some extra space?
# Hint 3
# What about storing sum frequencies in a hash table? Will it be useful?
# Hint 4
# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
# Similar Questions
# Two Sum
# Easy
# Continuous Subarray Sum
# Medium
# Subarray Product Less Than K
# Medium
# Find Pivot Index
# Easy
# Subarray Sums Divisible by K
# Medium
# Minimum Operations to Reduce X to Zero
# Medium
# K Radius Subarray Averages
# Medium
# Maximum Sum Score of Array
# Medium
# Discussion (214)