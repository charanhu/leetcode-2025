class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(current, open, close):
            print("current, open, close", current, open, close)
            if len(current)==2*n:
                result.append(current)
                return

            if open<n:
                backtrack(current+'(', open+1, close)

            if close<open:
                backtrack(current+')', open, close+1)

        result=[]
        backtrack("", 0, 0)
        return result




# 22. Generate Parentheses
# Solved
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.2M
# Submissions
# 2.8M
# Acceptance Rate
# 76.3%
# Topics
# String
# Dynamic Programming
# Backtracking
# Companies
# 0 - 3 months
# Amazon
# 19
# Google
# 16
# Meta
# 11
# Microsoft
# 3
# Bloomberg
# 3
# Apple
# 3
# Walmart Labs
# 2
# Grammarly
# 2
# 0 - 6 months
# Huawei
# 4
# TikTok
# 3
# Goldman Sachs
# 3
# Yandex
# 3
# Infosys
# 2
# Adobe
# 2
# 6 months ago
# Yahoo
# 14
# Uber
# 13
# Zoho
# 8
# J.P. Morgan
# 6
# ServiceNow
# 6
# Oracle
# 4
# Tesla
# 3
# DE Shaw
# 3
# Nvidia
# 3
# Texas Instruments
# 3
# Similar Questions
# Letter Combinations of a Phone Number
# Medium
# Valid Parentheses
# Easy
# Check if a Parentheses String Can Be Valid
# Medium
# Discussion (152)