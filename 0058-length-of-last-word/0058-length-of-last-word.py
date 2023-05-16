class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = [i for i in s.split(' ') if i!='']
        return len(new_s[-1])