class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        nums.sort()
        for i in range(k):
            element = nums[-1]
            score+=element
            nums.remove(nums[-1])
            nums.append(element+1)
        return score
        