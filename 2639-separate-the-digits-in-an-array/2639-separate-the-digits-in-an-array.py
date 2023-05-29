class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        seperated = []
        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    seperated.append(int(j))
            else:
                seperated.append(i)
        return seperated
