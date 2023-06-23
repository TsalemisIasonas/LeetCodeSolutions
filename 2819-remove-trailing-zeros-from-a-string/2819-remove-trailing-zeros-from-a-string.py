class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num.rstrip('0')
        if not num:
            return '0'
        return num