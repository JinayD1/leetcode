class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if (seen.get(num, None)) != None:
                return True
            seen.update({num: num})
        return False