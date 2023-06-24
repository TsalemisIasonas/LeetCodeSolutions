class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        occur = {}
        for i in nums:
            if i in occur:
                occur[i] += 1
            else:
                occur[i] = 1
        for i in occur.keys():
            if occur[i] > 1:
                res.append(i)
        return res