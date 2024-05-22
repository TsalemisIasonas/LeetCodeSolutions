class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            for j in nums:
                if abs(i-j) == k:
                    res+=1
        return res//2
        