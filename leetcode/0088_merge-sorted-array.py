class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1

        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1


# 88. Merge Sorted Array
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.1M
# Submissions
# 7.9M
# Acceptance Rate
# 51.9%
# Topics
# Array
# Two Pointers
# Sorting
# Companies
# 0 - 3 months
# Meta
# 95
# Google
# 53
# Amazon
# 27
# Microsoft
# 23
# Bloomberg
# 10
# Hubspot
# 5
# 0 - 6 months
# Accenture
# 4
# Yandex
# 3
# Infosys
# 2
# Apple
# 2
# Oracle
# 2
# Squarespace
# 2
# Canonical
# 2
# 6 months ago
# Adobe
# 48
# Uber
# 23
# Yahoo
# 20
# tcs
# 8
# TikTok
# 8
# IBM
# 6
# Zoho
# 6
# PayPal
# 6
# LinkedIn
# 4
# EPAM Systems
# 4
# Hint 1
# You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
# Hint 2
# If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.
# Similar Questions
# Merge Two Sorted Lists
# Easy
# Squares of a Sorted Array
# Easy
# Interval List Intersections
# Medium
# Take K of Each Character From Left and Right
# Medium
# Discussion (694)
