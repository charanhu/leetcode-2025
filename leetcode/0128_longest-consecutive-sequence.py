class Solution(object):
    # Define the method 'longestConsecutive' which takes a list of integers 'nums'
    def longestConsecutive(self, nums):
        """
        This method returns the length of the longest consecutive elements sequence in the list 'nums'.
        It leverages a hash set for O(1) average-time lookups.
        
        :type nums: List[int]
        :rtype: int
        """
        
        # Convert the list 'nums' to a set called 'hash_set'.
        # This removes duplicates and allows for fast membership testing.
        hash_set = set(nums)
        
        # Determine the number of unique elements in the set.
        n = len(hash_set)
        
        # If there are no elements, return 0 because there is no consecutive sequence.
        if n == 0:
            return 0
        
        # If there is exactly one element, the longest consecutive sequence can only be of length 1.
        if n == 1:
            return 1
            
        # Initialize 'max_count' to keep track of the longest consecutive sequence length found.
        max_count = 0
        
        # Iterate over each unique element 'x' in the set.
        for x in hash_set:
            # Check if 'x' is the start of a sequence.
            # 'x' is a start if there is no number immediately before it (i.e., x - 1 is not in the set).
            if x - 1 not in hash_set:
                # Initialize a counter 'count' to 0 for the current sequence starting at 'x'.
                count = 0
                
                # While the number (x + count) is in the set,
                # it means the consecutive sequence continues.
                while x + count in hash_set:
                    # Increment 'count' to include this number in the current sequence.
                    count += 1
                
                # Update 'max_count' if the current sequence length 'count' is greater than the previous maximum.
                max_count = max(count, max_count)
        
        # After processing all elements, return the maximum consecutive sequence length found.
        return max_count


# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.3M
# Submissions
# 4.9M
# Acceptance Rate
# 47.3%
# Topics
# Array
# Hash Table
# Union Find
# Companies
# 0 - 3 months
# Amazon
# 14
# Google
# 13
# Bloomberg
# 12
# Meta
# 5
# Microsoft
# 5
# IBM
# 3
# 0 - 6 months
# TikTok
# 5
# Lyft
# 4
# Oracle
# 3
# Uber
# 3
# Zepto
# 3
# Infosys
# 2
# EPAM Systems
# 2
# Cisco
# 2
# Roblox
# 2
# 6 months ago
# Adobe
# 31
# Apple
# 18
# Yahoo
# 8
# Turing
# 4
# tcs
# 3
# ByteDance
# 3
# Walmart Labs
# 3
# Zoho
# 3
# DE Shaw
# 3
# ServiceNow
# 3
# Similar Questions
# Binary Tree Longest Consecutive Sequence
# Medium
# Find Three Consecutive Integers That Sum to a Given Number
# Medium
# Maximum Consecutive Floors Without Special Floors
# Medium
# Length of the Longest Alphabetical Continuous Substring
# Medium
# Find the Maximum Number of Elements in Subset
# Medium
# Discussion (335)