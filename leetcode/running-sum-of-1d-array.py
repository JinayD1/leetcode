class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
        for num in nums:
            result.append(result[-1] + num)
        
        return result[1:]