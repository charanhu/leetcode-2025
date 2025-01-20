class Solution(object):
    def commonPrefix(self, strs, substrs):
        for word in strs:
            if not word.startswith(substrs):
                return False
            # else:
            #     continue
        return True
        

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=lambda x: len(x))
        substr=strs[0]
        n=len(substr)
        while n>0:
            if self.commonPrefix(strs, substr):
                return substr
            else:
                n-=1
                substr=substr[:n]

        return ""



# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.1M
# Submissions
# 9.2M
# Acceptance Rate
# 44.6%
# Topics
# String
# Trie
# Companies
# 0 - 3 months
# Google
# 26
# Meta
# 22
# Amazon
# 19
# Bloomberg
# 7
# Microsoft
# 6
# Apple
# 4
# CME Group
# 3
# Deloitte
# 2
# Oracle
# 2
# EPAM Systems
# 2
# 0 - 6 months
# tcs
# 5
# Visa
# 4
# Accenture
# 4
# TikTok
# 3
# Infosys
# 2
# Revolut
# 2
# Yelp
# 2
# Deutsche Bank
# 2
# 6 months ago
# Adobe
# 65
# Uber
# 28
# Yahoo
# 15
# IBM
# 9
# Zoho
# 9
# SAP
# 6
# Turing
# 5
# Accolite
# 3
# Walmart Labs
# 3
# Cognizant
# 3
# Similar Questions
# Smallest Missing Integer Greater Than Sequential Prefix Sum
# Easy
# Find the Length of the Longest Common Prefix
# Medium
# Longest Common Suffix Queries
# Hard
# Discussion (419)