class Solution:
    def firstUniqChar(self, s: str) -> int:
        sMap = {}
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        
        for key in sMap.keys():
            if sMap[key] == 1:
                return s.find(key)
        return -1