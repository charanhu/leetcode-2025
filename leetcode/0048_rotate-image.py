class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        for mat in matrix:
            mat.reverse()


# 48. Rotate Image
# Solved
# Medium
# Topics
# Companies
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.1M
# Submissions
# 2.7M
# Acceptance Rate
# 76.9%
# Topics
# Array
# Math
# Matrix
# Companies
# 0 - 3 months
# Google
# 14
# Meta
# 10
# Amazon
# 10
# Bloomberg
# 5
# Microsoft
# 4
# Uber
# 3
# Infosys
# 2
# Nvidia
# 2
# Roblox
# 2
# Capital One
# 2
# 0 - 6 months
# Cisco
# 13
# IBM
# 10
# Apple
# 2
# 6 months ago
# Adobe
# 22
# Yahoo
# 14
# Oracle
# 7
# Tinkoff
# 6
# Zoho
# 6
# ConsultAdd
# 4
# Walmart Labs
# 3
# ZScaler
# 3
# AMD
# 3
# Flipkart
# 2
# Similar Questions
# Determine Whether Matrix Can Be Obtained By Rotation
# Easy
# Discussion (204)