class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge

        if len(s) != len(t):
            return False

        es = {}
        te = {}

        for x in range(len(s)):
            if s[x] in es:
                es[s[x]] += 1
            else:
                es[s[x]] = 1
            
            if t[x] in te:
                te[t[x]] += 1
            else:
                te[t[x]] = 1
        
        return es == te