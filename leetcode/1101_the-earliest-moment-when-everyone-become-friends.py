class UnionFind:
    def __init__(self, n):
        # Initialize the parent array where each element is its own parent.
        # For example, if n = 5, then parent = [0, 1, 2, 3, 4].
        self.parent = list(range(n))
        # Initialize the rank array to keep an estimate of the tree height.
        # All elements start with a rank (height) of 0.
        self.rank = [0] * n
        # Count of separate groups (initially, each element is its own group).
        self.count = n

    def find(self, x):
        # This method finds the root (representative) of the element x.
        # It uses an iterative approach with path compression (halving technique)
        # to flatten the structure and make future finds faster.
        while self.parent[x] != x:
            # Point x directly to its grandparent. This is path halving.
            self.parent[x] = self.parent[self.parent[x]]
            # Move x up one level in the tree.
            x = self.parent[x]
        # When x equals its parent, we have found the root.
        return x

    def union(self, x, y):
        # Merge the groups containing elements x and y.
        # First, find the roots of x and y.
        rootX = self.find(x)
        rootY = self.find(y)
        # If both elements already have the same root, they are in the same group.
        if rootX == rootY:
            return False
        # Union by rank: attach the tree with a smaller rank (shorter tree) to the one with a larger rank.
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            # If both trees have the same rank, attach one tree to the other (arbitrarily choose rootX)
            # and then increase the rank of the new root by 1.
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        # Since two groups have merged, decrease the count of groups by one.
        self.count -= 1
        # Return True indicating that a union (merge) occurred.
        return True

class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        # Sort the logs by timestamp.
        # Each log is of the form [timestamp, x, y],
        # so the lambda function sorts based on the first element (timestamp).
        logs.sort(key=lambda x: x[0])
        
        # Initialize the UnionFind structure for n individuals.
        uf = UnionFind(n)
        
        # Process each log in chronological order.
        for timestamp, x, y in logs:
            # Attempt to union the groups of x and y.
            # If union returns True, it means that x and y were in separate groups and are now merged.
            if uf.union(x, y):
                # After a successful merge, check if there's only one group left.
                # If uf.count equals 1, it means all individuals are connected.
                if uf.count == 1:
                    # Return the current timestamp as the earliest moment when everyone is connected.
                    return timestamp
        
        # If all logs are processed and not everyone is connected, return -1.
        return -1


# 1101. The Earliest Moment When Everyone Become Friends
# Solved
# Medium
# Topics
# Companies
# Hint
# There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

# Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

# Example 1:

# Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
# Output: 20190301
# Explanation: 
# The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
# The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
# The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
# The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
# The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
# The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
# Example 2:

# Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# Output: 3
# Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
 

# Constraints:

# 2 <= n <= 100
# 1 <= logs.length <= 104
# logs[i].length == 3
# 0 <= timestampi <= 109
# 0 <= xi, yi <= n - 1
# xi != yi
# All the values timestampi are unique.
# All the pairs (xi, yi) occur at most one time in the input.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 112.3K
# Submissions
# 171.2K
# Acceptance Rate
# 65.6%
# Topics
# Array
# Union Find
# Sorting
# Companies
# Hint 1
# Sort the log items by their timestamp.
# Hint 2
# How can we model this problem as a graph problem?
# Hint 3
# Let's use a union-find data structure. At the beginning we have a graph with N nodes but no edges.
# Hint 4
# Then we loop through the events and unite each node until the number of connected components reach to 1. Notice that each time two different connected components are united the number of connected components decreases by 1.
# Similar Questions
# Number of Provinces
# Medium
# Discussion (22)