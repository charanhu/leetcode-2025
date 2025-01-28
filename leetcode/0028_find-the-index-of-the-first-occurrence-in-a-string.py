class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack:
            return -1
        if not needle:
            return -1
        lps = self.build_lps(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def build_lps(self, pattren):
        lps = [0] * len(pattren)
        i, length = 1, 0
        while i < len(pattren):
            if pattren[i] == pattren[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3M
# Submissions
# 6.9M
# Acceptance Rate
# 44.2%
# Topics
# Two Pointers
# String
# String Matching
# Companies
# 0 - 3 months
# Google
# 16
# Meta
# 5
# Microsoft
# 5
# Amazon
# 4
# Bloomberg
# 4
# tcs
# 3
# Expedia
# 2
# 6 months ago
# Apple
# 17
# Adobe
# 12
# Uber
# 12
# Yahoo
# 10
# Warnermedia
# 5
# Zoho
# 3
# Accenture
# 3
# IBM
# 2
# Infosys
# 2
# LinkedIn
# 2
# Similar Questions
# Shortest Palindrome
# Hard
# Repeated Substring Pattern
# Easy
# Discussion (325)