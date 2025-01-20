# merge-strings-alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        s = ""
        if n == m:
            for i in range(n):
                s = s + word1[i] + word2[i]
        if n < m:
            k = 0
            for i in range(n):
                s = s + word1[i] + word2[i]
                k = k + 1
            s = s + word2[k:]
        if n > m:
            k = 0
            for i in range(m):
                s = s + word1[i] + word2[i]
                k = k + 1
            s = s + word1[k:]
        return s



# 1768. Merge Strings Alternately
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.3M
# Submissions
# 1.6M
# Acceptance Rate
# 81.5%
# Topics
# Two Pointers
# String
# Companies
# 0 - 3 months
# Google
# 58
# Amazon
# 25
# Meta
# 15
# Microsoft
# 15
# Bloomberg
# 2
# Wells Fargo
# 2
# 0 - 6 months
# Zoho
# 2
# Uber
# 2
# 6 months ago
# Apple
# 31
# Adobe
# 28
# Yahoo
# 10
# Walmart Labs
# 2
# Hint 1
# Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.
# Similar Questions
# Zigzag Iterator
# Medium
# Minimum Additions to Make Valid String
# Medium
# Discussion (201)