class Solution:
    def divisorGame(self, n: int) -> bool:
        if n < 1:
            return False
        return n%2 == 0



# 1025. Divisor Game
# Solved
# Easy
# Topics
# Companies
# Hint
# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.

# Return true if and only if Alice wins the game, assuming both players play optimally.

 

# Example 1:

# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:

# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

# Constraints:

# 1 <= n <= 1000
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 301.9K
# Submissions
# 432.1K
# Acceptance Rate
# 69.9%
# Topics
# Math
# Dynamic Programming
# Brainteaser
# Game Theory
# Companies
# Hint 1
# If the current number is even, we can always subtract a 1 to make it odd. If the current number is odd, we must subtract an odd number to make it even.
# Discussion (111)