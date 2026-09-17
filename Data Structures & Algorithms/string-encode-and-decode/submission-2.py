class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        sent = []
        x = 0
    # "4#toom3#bee3#run
        while x < len(s):
            y = x
            while s[y] != "#":
                y+=1
            length = int(s[x:y])
            sent += [s[y+1:y+1+length]]
            x = y+length+1
        return sent





