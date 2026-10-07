class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        l = 0
        tmp = {}
        for c in t:
            tmp[c] = 1 + tmp.get(c, 0)

        minsubstring = [-1, -1]
        length = float("infinity")
        smp = {}
        have, need = 0, len(tmp)
        for r in range(len(s)):
            smp[s[r]] = 1 + smp.get(s[r], 0)

            if s[r] in tmp and smp[s[r]] == tmp[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    length = r - l + 1
                    minsubstring = [l,r]

                smp[s[l]] -= 1
                if s[l] in tmp and smp[s[l]] < tmp[s[l]]:
                    have -= 1
                l += 1

        l, r = minsubstring
        return s[l:r+1] if length != float("infinity") else ""
                

            