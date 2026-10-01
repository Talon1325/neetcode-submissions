class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = str(len(s))
            res += length + "#" + s
            
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        numstart = 0

        while numstart < len(s):
            numend = numstart
            while s[numend] != "#":
                numend += 1
            length = int(s[numstart:numend])
            stringstart = numend + 1
            stringend = stringstart + length
            res.append(s[stringstart:stringend])
            numstart = stringend
            
        return res