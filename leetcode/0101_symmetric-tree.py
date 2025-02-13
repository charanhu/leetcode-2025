# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Helper function that checks if two trees (or subtrees) are mirror images of each other.
    def isMirror(self, node1, node2):
        # If both nodes are None, then they are mirrors (both are empty).
        if not node1 and not node2:
            return True
        
        # If one of the nodes is None (but not both), then the trees cannot be mirrors.
        if not node1 or not node2:
            return False
        
        # Both nodes are not None: check that the current node values are equal.
        # Also, recursively check that the left subtree of node1 is a mirror of the right subtree of node2,
        # and the right subtree of node1 is a mirror of the left subtree of node2.
        return (node1.val == node2.val and 
                self.isMirror(node1.left, node2.right) and 
                self.isMirror(node1.right, node2.left))

    # Main function to check if the tree is symmetric.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Conventionally, an empty tree is symmetric.
        if not root:
            return True  # Change to True if you consider an empty tree symmetric.
        
        # Check if the left and right subtrees of the root are mirrors of each other.
        return self.isMirror(root.left, root.right)



# METHOD 2

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, by convention, it is symmetric.
        # (Some definitions consider an empty tree symmetric.)
        if not root:
            return True
        
        # Initialize a deque (double-ended queue) for BFS.
        # Start by enqueuing the left and right children of the root.
        queue = deque([root.left, root.right])
        
        # Process nodes in pairs from the queue until the queue is empty.
        while queue:
            # Remove the first two nodes from the queue.
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            # If both nodes are None, they are symmetric at this level.
            # Continue with the next pair.
            if not node1 and not node2:
                continue
            
            # If one node is None (but not both) or the values differ,
            # the tree is not symmetric.
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Enqueue the children of the nodes in mirror order:
            # - The left child of node1 should match the right child of node2.
            # - The right child of node1 should match the left child of node2.
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        # If all node pairs are symmetric, return True.
        return True
