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
