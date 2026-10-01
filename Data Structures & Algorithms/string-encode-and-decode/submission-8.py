class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1"
        if len(strs) == 0:
            return ""
        mystring = strs[0]
        for s in range(1, len(strs)):
            mystring = mystring +  "~$~" + strs[s] 
        return mystring
    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        if s == "":
            return [""]
        strs = s.split("~$~")
        return strs