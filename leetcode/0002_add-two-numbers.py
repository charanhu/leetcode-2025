# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        return self.addTwoLists(l1, l2, 0)

    def addTwoLists(self, l1, l2, carry):
        # Base case: if both lists are empty and carry is 0, no more to add
        if not l1 and not l2 and carry == 0:
            return None

        # Get current values (if node is present, else 0)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Sum them with the carry
        total = val1 + val2 + carry

        # Determine new digit and new carry
        new_digit = total % 10
        new_carry = total // 10

        # Create the node for this digit
        current_node = ListNode(new_digit)

        # Move to the next nodes if they exist
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None

        # Recursively set the .next for the current node
        current_node.next = self.addTwoLists(next1, next2, new_carry)

        return current_node