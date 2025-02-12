# Method 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to serialize a binary tree.
        # We use a preorder traversal and include a marker (e.g., "#") for null nodes.
        # The comma delimiter ensures that node values and markers don't merge into false matches.
        def serialize(node):
            if not node:
                return ",#"  # marker for null
            # Preorder: Node, then left, then right.
            # Adding a leading comma helps avoid merging adjacent values.
            return "," + str(node.val) + serialize(node.left) + serialize(node.right)
        
        # Serialize the main tree and the subtree.
        tree_serial = serialize(root)
        subtree_serial = serialize(subRoot)
        
        # Debug print (optional):
        # print("Tree:", tree_serial)
        # print("Subtree:", subtree_serial)
        
        # Check if the serialization of subRoot is a substring of the serialization of root.
        # This works because our serialization uniquely represents the structure and node values.
        return subtree_serial in tree_serial




# Method 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: If subRoot is None, an empty tree is always considered a subtree.
        if not subRoot:
            return True
        # Base case: If root is None but subRoot is not, then subRoot cannot be a subtree.
        if not root:
            return False

        # Helper function to determine if two trees are exactly the same.
        # This function checks if the tree rooted at 'node1' is identical in structure and node values to the tree rooted at 'node2'.
        def isSameTree(node1, node2):
            # If both nodes are None, then both trees are empty and thus identical.
            if not node1 and not node2:
                return True
            # If one of the nodes is None (but not both), the trees differ.
            if not node1 or not node2:
                return False
            # Check if the current nodes have the same value, and then recursively check:
            #   - The left subtrees of both nodes.
            #   - The right subtrees of both nodes.
            return (node1.val == node2.val and 
                    isSameTree(node1.left, node2.left) and 
                    isSameTree(node1.right, node2.right))

        # DFS (Depth-First Search) function to traverse the main tree.
        # This function checks if there exists a node in the main tree such that the subtree rooted at that node
        # is identical to 'subRoot'.
        def dfs(node):
            # If we reach a null node in the main tree, we have no subtree here, so return False.
            if not node:
                return False
            # Check if the subtree starting at the current node is exactly the same as subRoot.
            # Use our helper function 'isSameTree' for deep comparison.
            if isSameTree(node, subRoot):
                return True
            # Recursively search for a matching subtree in the left and right children.
            # If either recursive call returns True, then subRoot is a subtree.
            return dfs(node.left) or dfs(node.right)

        # Start the DFS traversal from the root of the main tree.
        return dfs(root)



# 572. Subtree of Another Tree
# Solved
# Easy
# Topics
# Companies
# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1M
# Submissions
# 2M
# Acceptance Rate
# 49.4%
# Topics
# Companies
# 0 - 6 months
# Amazon
# 4
# Google
# 3
# Compass
# 2
# 6 months ago
# Meta
# 8
# Microsoft
# 4
# TikTok
# 3
# Uber
# 3
# Morgan Stanley
# 2
# eBay
# 2
# Jump Trading
# 2
# Hint 1
# Which approach is better here- recursive or iterative?
# Hint 2
# If recursive approach is better, can you write recursive function with its parameters?
# Hint 3
# Two trees s and t are said to be identical if their root values are same and their left and right subtrees are identical. Can you write this in form of recursive formulae?
# Hint 4
# Recursive formulae can be: isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)
# Similar Questions
# Count Univalue Subtrees
# Medium
# Most Frequent Subtree Sum
# Medium
# Discussion (110)