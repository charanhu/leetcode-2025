class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n<2:
            return
        max_water=0
        i=0
        j=n-1
        while i<j:
            water=0
            if height[i]<=height[j]:
                water=height[i]*(j-i)
                if max_water<water:
                    max_water=water
                i+=1
            else:
                water=height[j]*(j-i)
                if max_water<water:
                    max_water=water
                j-=1
        return max_water



        

# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.7M
# Submissions
# 6.5M
# Acceptance Rate
# 56.9%
# Topics
# Array
# Two Pointers
# Greedy
# Companies
# 0 - 3 months
# Google
# 17
# Amazon
# 6
# Bloomberg
# 6
# Microsoft
# 4
# 0 - 6 months
# Meta
# 4
# Goldman Sachs
# 3
# SAP
# 3
# Adobe
# 2
# Snowflake
# 2
# 6 months ago
# Apple
# 29
# Yahoo
# 24
# Uber
# 16
# Oracle
# 14
# Flipkart
# 11
# Yandex
# 9
# TikTok
# 8
# Zoho
# 7
# tcs
# 5
# Tesla
# 5
# Hint 1
# If you simulate the problem, it will be O(n^2) which is not efficient.
# Hint 2
# Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
# Hint 3
# How can you calculate the amount of water at each step?
# Similar Questions
# Trapping Rain Water
# Hard
# Maximum Tastiness of Candy Basket
# Medium
# House Robber IV
# Medium
# Discussion (473)