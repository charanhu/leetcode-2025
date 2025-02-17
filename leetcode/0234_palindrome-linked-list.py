# Method 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: an empty list or a single-node list is always a palindrome.
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the list using two pointers.
        # 'fast' moves two steps at a time and 'slow' moves one step.
        # When fast reaches the end, slow will be at the middle.
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Step 2: Handle odd-length lists.
        # If fast is not None, it means the list has an odd number of nodes.
        # In that case, skip the middle node since it doesn't affect the palindrome property.
        if fast is not None:
            slow = slow.next
        
        # Step 3: Reverse the second half of the list starting from 'slow'.
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next  # Save the next node.
            curr.next = prev       # Reverse the pointer of the current node.
            prev = curr            # Move 'prev' one step forward.
            curr = next_temp       # Move to the next node.
        # Now, 'prev' is the head of the reversed second half of the list.
        
        # Step 4: Compare the first half with the reversed second half.
        first_half = head
        second_half = prev
        while second_half:
            # If any corresponding nodes differ, the list is not a palindrome.
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # If we complete the comparison without mismatches, it's a palindrome.
        return True




# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.3M
# Submissions
# 4.1M
# Acceptance Rate
# 55.0%
# Topics
# Linked List
# Two Pointers
# Stack
# Recursion
# Companies
# 0 - 3 months
# Google
# 12
# Amazon
# 8
# Meta
# 5
# Bloomberg
# 4
# 0 - 6 months
# Microsoft
# 3
# IXL
# 2
# 6 months ago
# Apple
# 16
# Adobe
# 9
# Uber
# 8
# Yandex
# 5
# Yahoo
# 3
# Oracle
# 2
# Zoho
# 2
# Intuit
# 2
# Qualcomm
# 2
# Devsinc
# 2
# Similar Questions
# Palindrome Number
# Easy
# Valid Palindrome
# Easy
# Reverse Linked List
# Easy
# Maximum Twin Sum of a Linked List
# Medium
# Discussion (273)