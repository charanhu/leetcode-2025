class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ts = Trie()
        for word in strs:
            ts.insert(word)
        return ts.common_prefix()


class TrieNode:
    def __init__(self):
        self.childnode = {}
        self.endofword = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0

    def insert(self, word):
        self.root.count += 1
        self.total_words += 1

        current = self.root
        for ch in word:
            if ch not in current.childnode:
                current.childnode[ch] = TrieNode()
            current = current.childnode[ch]
            current.count += 1
        current.endofword = True

    def common_prefix(self):
        pref = ""
        current = self.root

        while True:
            if len(current.childnode) == 1:
                (ch, nextnode) = list(current.childnode.items())[0]
                if nextnode.count == self.total_words:
                    pref += ch
                    current = nextnode
                else:
                    break
            else:
                break
        return pref
    


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