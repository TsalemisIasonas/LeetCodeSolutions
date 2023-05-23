class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        for i in str(n):
            digits.append(int(i))
        product = 1
        for i in digits:
            product *= i
        return (product - sum(digits))