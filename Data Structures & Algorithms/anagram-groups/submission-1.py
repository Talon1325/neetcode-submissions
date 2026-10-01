class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allcount = defaultdict(list)
        for i in range(len(strs)):
            count = [0]*26
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            allcount[tuple(count)].append(strs[i])

        return list(allcount.values())