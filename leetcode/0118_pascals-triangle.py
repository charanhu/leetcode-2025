class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1, i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle
    

#     118. Pascal's Triangle
# Solved
# Easy
# Topics
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2M
# Submissions
# 2.6M
# Acceptance Rate
# 76.1%
# Topics
# Array
# Dynamic Programming
# Companies
# 0 - 3 months
# Google
# 12
# Amazon
# 6
# Meta
# 5
# Bloomberg
# 4
# 0 - 6 months
# Microsoft
# 4
# Mitsogo
# 3
# Apple
# 2
# 6 months ago
# Adobe
# 18
# Uber
# 10
# Yahoo
# 9
# Goldman Sachs
# 3
# Accenture
# 3
# Virtusa
# 3
# J.P. Morgan
# 2
# Deloitte
# 2
# tcs
# 2
# Oracle
# 2
# Similar Questions
# Pascal's Triangle II
# Easy
# Discussion (170)