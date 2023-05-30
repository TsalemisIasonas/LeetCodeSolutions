class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digits = []
        for num in nums:
            for digit in str(num):
                digits.append(int(digit))
        el_sum = sum(nums)
        digit_sum = sum(digits)
        return abs(digit_sum - el_sum)