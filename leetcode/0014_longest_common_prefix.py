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
