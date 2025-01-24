class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            return sorted(s)==sorted(t)
        return False

        
# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.3M
# Submissions
# 6.6M
# Acceptance Rate
# 65.9%
# Topics
# Hash Table
# String
# Sorting
# Companies
# 0 - 3 months
# Bloomberg
# 12
# Google
# 10
# Microsoft
# 6
# Meta
# 5
# Amazon
# 4
# Oracle
# 3
# Affirm
# 3
# Infosys
# 2
# 0 - 6 months
# Apple
# 4
# EPAM Systems
# 2
# 6 months ago
# Adobe
# 12
# Uber
# 11
# Yahoo
# 9
# tcs
# 7
# Accenture
# 5
# Yandex
# 4
# Goldman Sachs
# 3
# J.P. Morgan
# 2
# Walmart Labs
# 2
# TikTok
# 2
# Similar Questions
# Group Anagrams
# Medium
# Palindrome Permutation
# Easy
# Find All Anagrams in a String
# Medium
# Find Resultant Array After Removing Anagrams
# Easy
# Discussion (234)