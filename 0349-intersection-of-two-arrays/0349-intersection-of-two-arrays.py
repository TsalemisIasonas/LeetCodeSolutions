class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in nums1:
            for j in range(len(nums2)):
                if nums2[j] == i and i not in arr:
                    arr.append(i)
        return arr