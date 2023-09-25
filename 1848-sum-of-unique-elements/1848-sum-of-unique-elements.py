class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_set = set()
        non_unique_set = set()

        for num in nums:
            if num in unique_set:
                non_unique_set.add(num)
            else:
                unique_set.add(num)

        unique_elements = unique_set - non_unique_set  
        return sum(unique_elements)
            