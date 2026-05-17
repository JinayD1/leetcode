class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []

        for num in nums1:
            if (num in nums2) and (num not in intersect):
                intersect.append(num)
        return intersect