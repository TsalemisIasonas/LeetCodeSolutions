class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0<=i and i<j and j<len(nums) and nums[i]+nums[j] < target:
                    pairs+=1
        return pairs
        