class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Get the number of rows and columns in the matrix.
        n = len(matrix)          # Number of rows
        m = len(matrix[0])       # Number of columns
        
        # Create a DP table with the same dimensions as the matrix.
        # dp[i][j] will store the side length of the largest square ending at cell (i, j).
        dp = [[0] * m for _ in range(n)]
        
        # Initialize a variable to keep track of the maximum side length found.
        max_sq = 0
        
        # Loop over each cell in the matrix.
        for i in range(n):
            for j in range(m):
                # Check if the current cell has a "1" (note: the matrix contains strings).
                if matrix[i][j] == "1":
                    # For cells in the first row or first column, the largest square ending here is just 1.
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # For other cells, find the minimum side length of the square that can be formed
                        # using the top cell, left cell, and top-left diagonal cell.
                        # Adding 1 extends that square to include the current cell.
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Update the maximum square side length if a larger square is found.
                    max_sq = max(max_sq, dp[i][j])
                else:
                    # If the current cell is "0", no square of 1's can end at this cell.
                    dp[i][j] = 0
        
        # The problem asks for the area of the largest square.
        # Multiply the side length by itself to obtain the area.
        return max_sq * max_sq




# 221. Maximal Square
# Solved
# Medium
# Topics
# Companies
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 776.3K
# Submissions
# 1.6M
# Acceptance Rate
# 48.1%
# Topics
# Array
# Dynamic Programming
# Matrix
# Companies
# 0 - 3 months
# Google
# 9
# PayPal
# 5
# Oracle
# 2
# Nvidia
# 2
# 0 - 6 months
# Wise
# 10
# Amazon
# 5
# Microsoft
# 3
# TikTok
# 3
# PhonePe
# 3
# ByteDance
# 2
# Goldman Sachs
# 2
# Booking.com
# 2
# SAP
# 2
# 6 months ago
# Meta
# 5
# Apple
# 5
# Adobe
# 4
# Walmart Labs
# 4
# ServiceNow
# 4
# Salesforce
# 4
# BharatPe
# 4
# DE Shaw
# 3
# Uber
# 3
# Citadel
# 3
# Similar Questions
# Maximal Rectangle
# Hard
# Largest Plus Sign
# Medium
# Count Artifacts That Can Be Extracted
# Medium
# Stamping the Grid
# Hard
# Maximize Area of Square Hole in Grid
# Medium
# Discussion (66)