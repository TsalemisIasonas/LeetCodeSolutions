class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        res = ''
        for i in range(len(num)):
            if num[i] == "6":
                num = num[:i] + "9" + num[i+1:]
                break
        return int(num)
