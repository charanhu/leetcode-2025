class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)    # number of rows
        n = len(matrix[0]) # number of columns, not needed for this operation
        zeros=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zeros.append([i, j])
        for zero in zeros:
            k, v = zero[0], zero[1]
            for row in range(m):
                matrix[row][v]=0
            for col in range(n):
                matrix[k][col]=0

# 73. Set Matrix Zeroes
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.8M
# Submissions
# 3M
# Acceptance Rate
# 58.5%
# Topics
# Array
# Hash Table
# Matrix
# Companies
# 0 - 3 months
# Google
# 5
# Meta
# 3
# Bloomberg
# 3
# 0 - 6 months
# Microsoft
# 6
# Amazon
# 5
# Oracle
# 3
# Goldman Sachs
# 2
# 6 months ago
# Adobe
# 26
# Apple
# 12
# Uber
# 8
# Yahoo
# 7
# Juspay
# 3
# Sprinklr
# 3
# Expedia
# 3
# Zoho
# 2
# Nvidia
# 2
# Accenture
# 2
# Hint 1
# If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
# Hint 2
# Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
# Hint 3
# We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
# Hint 4
# We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.
# Similar Questions
# Discussion (130)