class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += str(x) + "#"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0
        while x != len(s):
            st = ""
            while s[x] != "#":
                st += s[x]
                x+=1
            res.append(st)
            x+=1
            
        return res

