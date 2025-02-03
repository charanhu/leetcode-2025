class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n%2==0:
            return half * half
        else:
            return half * half * x
        
# 50. Pow(x, n)
# Solved
# Medium
# Topics
# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2M
# Submissions
# 5.6M
# Acceptance Rate
# 36.3%
# Topics
# Math
# Recursion
# Companies
# 0 - 3 months
# Meta
# 68
# Google
# 13
# Amazon
# 10
# Bloomberg
# 3
# ServiceNow
# 2
# 0 - 6 months
# Microsoft
# 11
# Oracle
# 2
# Citadel
# 2
# 6 months ago
# Apple
# 15
# Adobe
# 11
# Uber
# 8
# Goldman Sachs
# 7
# Yahoo
# 6
# LinkedIn
# 4
# Walmart Labs
# 4
# TikTok
# 4
# Salesforce
# 3
# J.P. Morgan
# 2
# Similar Questions
# Sqrt(x)
# Easy
# Super Pow
# Medium
# Count Collisions of Monkeys on a Polygon
# Medium
# Discussion (398)