class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return
        visited=[]
        top, bottom = 0, len(matrix)-1
        left, right= 0, len(matrix[0])-1
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                visited.append(matrix [top][i])
            top+=1
            if top<=bottom and left<=right:
                for i in range(top, bottom+1):
                    visited.append(matrix[i][right])
                right-=1
            if top<=bottom and left<=right:
                for i in range(right, left-1, -1):
                    visited.append(matrix[bottom][i])
                bottom-=1
            if top<=bottom and left<=right:
                for i in range(bottom, top-1, -1):
                    visited.append(matrix[i][left])
                left+=1
        return visited


# 54. Spiral Matrix
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.8M
# Submissions
# 3.3M
# Acceptance Rate
# 52.6%
# Topics
# Array
# Matrix
# Simulation
# Companies
# 0 - 3 months
# Amazon
# 13
# Google
# 12
# Microsoft
# 6
# Uber
# 6
# Meta
# 5
# Cisco
# 4
# TikTok
# 3
# Capital One
# 3
# Bloomberg
# 2
# Zoho
# 2
# 0 - 6 months
# Oracle
# 5
# Epic Systems
# 4
# Roblox
# 3
# eBay
# 3
# IBM
# 2
# Infosys
# 2
# Nordstrom
# 2
# Intuit
# 2
# Databricks
# 2
# PayPal
# 2
# 6 months ago
# Apple
# 33
# Adobe
# 27
# Walmart Labs
# 7
# Accenture
# 7
# Yahoo
# 7
# tcs
# 4
# Epic Games
# 4
# Goldman Sachs
# 3
# DE Shaw
# 3
# Darwinbox
# 3
# Hint 1
# Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
# Hint 2
# We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
# Hint 3
# Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.
# Similar Questions
# Spiral Matrix II
# Medium
# Spiral Matrix III
# Medium
# Spiral Matrix IV
# Medium
# Discussion (191)