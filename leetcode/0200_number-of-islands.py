class Solution(object):
    def dfs(self, grid, i, j, m, n):
        # Boundary checks
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        
        # Mark the current cell as visited by setting it to '0'
        grid[i][j] = '0'
        
        # Explore all adjacent cells (up, down, left, right)
        self.dfs(grid, i-1, j, m, n)  # Up
        self.dfs(grid, i+1, j, m, n)  # Down
        self.dfs(grid, i, j-1, m, n)  # Left
        self.dfs(grid, i, j+1, m, n)  # Right

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0  # Empty grid
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1  # Found a new island
                    self.dfs(grid, i, j, m, n)  # Mark all cells in this island as visited
        
        return count


# 200. Number of Islands
# Solved
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.2M
# Submissions
# 5.2M
# Acceptance Rate
# 61.2%
# Topics
# Array
# Depth-First Search
# Breadth-First Search
# Union Find
# Matrix
# Companies
# 0 - 3 months
# Amazon
# 53
# Google
# 19
# Bloomberg
# 18
# Meta
# 12
# Microsoft
# 10
# Uber
# 9
# TikTok
# 7
# LinkedIn
# 4
# Apple
# 4
# Anduril
# 4
# 0 - 6 months
# Oracle
# 10
# Yandex
# 5
# Tinkoff
# 4
# Adobe
# 4
# Nvidia
# 4
# Salesforce
# 4
# Whatnot
# 4
# Zoho
# 3
# PayPal
# 3
# Qualcomm
# 3
# 6 months ago
# Goldman Sachs
# 19
# Samsung
# 13
# Yahoo
# 9
# ByteDance
# 7
# Tesla
# 7
# Intel
# 7
# Walmart Labs
# 6
# Flipkart
# 5
# Siemens
# 5
# eBay
# 5
# Similar Questions
# Surrounded Regions
# Medium
# Walls and Gates
# Medium
# Number of Islands II
# Hard
# Number of Connected Components in an Undirected Graph
# Medium
# Battleships in a Board
# Medium
# Number of Distinct Islands
# Medium
# Max Area of Island
# Medium
# Count Sub Islands
# Medium
# Find All Groups of Farmland
# Medium
# Count Unreachable Pairs of Nodes in an Undirected Graph
# Medium
# Maximum Number of Fish in a Grid
# Medium
# Discussion (237)