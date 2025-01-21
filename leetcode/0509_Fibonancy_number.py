class Solution(object):
    def __init__(self):
        self.memo = {}  # Initialize memo once for the instance

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            self.memo[0] = 0
            return 0
        if n == 1:
            self.memo[1] = 1
            return 1
        
        # Recursively compute while storing results in memo
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]






# another
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0 
        b = 1 
        Sum = 0
        if n<=1: 
            return n
        for i in range(2,n+1):
            Sum = a + b
            a = b 
            b = Sum 
        return Sum  
        



# 509. Fibonacci Number
# Solved
# Easy
# Topics
# Companies
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.2M
# Submissions
# 3M
# Acceptance Rate
# 72.3%
# Topics
# Math
# Dynamic Programming
# Recursion
# Memoization
# Companies
# 0 - 3 months
# Amazon
# 8
# Google
# 3
# Meta
# 3
# Apple
# 2
# 0 - 6 months
# Nvidia
# 3
# Microsoft
# 2
# Accenture
# 2
# 6 months ago
# tcs
# 12
# Adobe
# 6
# Bloomberg
# 4
# Uber
# 4
# Cognizant
# 3
# Yahoo
# 3
# Capgemini
# 3
# J.P. Morgan
# 2
# Infosys
# 2
# Goldman Sachs
# 2
# Similar Questions
# Climbing Stairs
# Easy
# Split Array into Fibonacci Sequence
# Medium
# Length of Longest Fibonacci Subsequence
# Medium
# N-th Tribonacci Number