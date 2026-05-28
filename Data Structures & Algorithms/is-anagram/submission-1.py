class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(1)
            return False

        shash = {}
        thash = {}

        for x in range(len(s)): # 0(n)
            shash[s[x]] = 1 + shash.get(s[x], 0)
            thash[t[x]] = 1 + thash.get(t[x], 0)
        return thash == shash

        