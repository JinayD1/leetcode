class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need this for when t smaller in length than s
        if len(s) != len(t): return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for ch in t:
            if count.get(ch, None) == None or count.get(ch, 0) == 0:
                return False
            count[ch] -= 1
        return True