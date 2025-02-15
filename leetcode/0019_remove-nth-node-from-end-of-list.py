# Method 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # If the list is empty, there is nothing to remove.
        if not head:
            return None

        # Create a dummy node that points to the head.
        # This dummy node helps to handle edge cases such as removing the head itself.
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers: slow and fast.
        # Both start from the dummy node.
        slow = dummy
        fast = dummy

        # Move the fast pointer ahead by n+1 steps.
        # The extra 1 step ensures that the gap between slow and fast is n nodes.
        # When fast reaches the end, slow will be exactly before the node to remove.
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers at the same pace until the fast pointer reaches the end of the list.
        # Since fast started n+1 steps ahead, slow will land right before the target node.
        while fast:
            slow = slow.next
            fast = fast.next

        # Skip over the target node.
        # slow.next is the node that needs to be removed.
        # We bypass it by setting slow.next to slow.next.next.
        slow.next = slow.next.next

        # Return the new head of the list.
        # dummy.next points to the head of the updated list, handling the case where the original head was removed.
        return dummy.next


# Method 2 (my method])
# The approach here is to remove the nth node from the end by:
# 1. Reversing the linked list.
# 2. Removing the nth node from the start of the reversed list.
# 3. Reversing the list again to restore the original order (minus the removed node).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # If the list is empty, there's nothing to remove.
        if not head:
            return
        
        # === Step 1: Reverse the Linked List ===
        # We'll reverse the entire list so that the nth node from the end becomes the nth node from the beginning.
        curr = head
        prev = None
        while curr:
            temp = curr.next   # Store the next node temporarily.
            curr.next = prev   # Reverse the pointer: current node now points to the previous node.
            prev = curr        # Move the prev pointer to the current node.
            curr = temp        # Move to the next node in the original list.
        
        # After reversal, 'prev' is the new head of the reversed list.
        head = prev
        
        # === Step 2: Remove the nth Node from the Reversed List ===
        # Now the problem is reduced to removing the nth node from the beginning.
        curr = head
        if n == 1:
            # Special case: if n == 1, we need to remove the first node of the reversed list.
            head = curr.next  # Set head to the second node, effectively removing the first.
            del curr          # Delete the node (optional in Python, but indicates removal).
        else:
            # For n > 1, traverse the list to reach the node just before the nth node.
            prev = curr
            i = 1  # Start counting from 1 since we're already at the first node.
            while curr:
                curr = curr.next  # Move to the next node.
                i += 1            # Increment the counter.
                if i == n:
                    # When counter equals n, curr is at the nth node to be removed.
                    # 'prev' points to the node just before the one we want to remove.
                    prev.next = curr.next  # Bypass the nth node.
                    del curr               # Delete the node (optional).
                    break
                prev = curr  # Move the prev pointer along as we traverse.
        
        # === Step 3: Reverse the List Again to Restore Original Order ===
        # Reverse the list back to its original order (minus the removed node).
        curr = head
        prev = None
        while curr:
            temp = curr.next   # Store the next node.
            curr.next = prev   # Reverse the pointer.
            prev = curr        # Move prev forward.
            curr = temp        # Move to the next node.
        
        # After reversing back, 'prev' is the head of the final, updated list.
        return prev




# 19. Remove Nth Node From End of List
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.3M
# Submissions
# 6.8M
# Acceptance Rate
# 47.9%
# Topics
# Linked List
# Two Pointers
# Companies
# 0 - 3 months
# Meta
# 24
# Google
# 12
# Amazon
# 6
# Microsoft
# 3
# tcs
# 3
# Apple
# 2
# 0 - 6 months
# Bloomberg
# 3
# 6 months ago
# Adobe
# 9
# Oracle
# 8
# Uber
# 5
# Yahoo
# 5
# TikTok
# 2
# Nvidia
# 2
# PayPal
# 2
# Qualcomm
# 2
# Capgemini
# 2
# Hint 1
# Maintain two pointers and update one with a delay of n steps.
# Similar Questions
# Swapping Nodes in a Linked List
# Medium
# Delete N Nodes After M Nodes of a Linked List
# Easy
# Delete the Middle Node of a Linked List
# Medium
# Discussion (232)