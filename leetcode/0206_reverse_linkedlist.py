# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        return prev
        

# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4.9M
# Submissions
# 6.2M
# Acceptance Rate
# 78.4%
# Topics
# Linked List
# Recursion
# Companies
# 0 - 3 months
# Google
# 12
# Bloomberg
# 6
# Microsoft
# 5
# Amazon
# 5
# Meta
# 4
# Oracle
# 4
# TikTok
# 3
# Apple
# 2
# SAP
# 2
# 0 - 6 months
# Nvidia
# 3
# Adobe
# 2
# 6 months ago
# Yahoo
# 9
# Yandex
# 8
# tcs
# 6
# Uber
# 5
# Qualcomm
# 4
# Siemens
# 3
# PayPal
# 3
# Deutsche Bank
# 3
# J.P. Morgan
# 2
# ByteDance
# 2
# Similar Questions
# Reverse Linked List II
# Medium
# Binary Tree Upside Down
# Medium
# Palindrome Linked List
# Easy
# Reverse Nodes in Even Length Groups
# Medium
# Maximum Twin Sum of a Linked List
# Medium
# Remove Nodes From Linked List
# Medium
# Insert Greatest Common Divisors in Linked List
# Medium
# Discussion (259)