class Solution(object):
    def nextPermutation(self, nums):
        """
        Modify the list nums to its next permutation in place.
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return  # No permutation needed for arrays of size 0 or 1

        # Step 1: Find the Pivot
        pivot = -1  # Initialize pivot index
        for i in range(n - 2, -1, -1):  # Start from second last element
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            # The array is in descending order; reverse it to the smallest permutation
            nums.reverse()
            return

        # Step 2: Find the Right Successor to the Pivot
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break

        # Step 3: Swap the Pivot with the Successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # Step 4: Reverse the Suffix After the Pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# 31. Next Permutation
# Solved
# Medium
# Topics
# Companies
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.7M
# Submissions
# 3.9M
# Acceptance Rate
# 42.0%
# Topics
# Array
# Two Pointers
# Companies
# 0 - 3 months
# Meta
# 30
# Google
# 18
# Amazon
# 7
# Microsoft
# 5
# Bloomberg
# 3
# Oracle
# 2
# 0 - 6 months
# TikTok
# 4
# Adobe
# 3
# Mitsogo
# 3
# DoorDash
# 3
# Nike
# 2
# 6 months ago
# J.P. Morgan
# 28
# Apple
# 19
# Uber
# 15
# Yahoo
# 8
# Infosys
# 5
# Goldman Sachs
# 5
# Paytm
# 5
# DE Shaw
# 3
# Arcesium
# 3
# VMware
# 3
# Similar Questions
# Permutations
# Medium
# Permutations II
# Medium
# Permutation Sequence
# Hard
# Palindrome Permutation II
# Medium
# Minimum Adjacent Swaps to Reach the Kth Smallest Number