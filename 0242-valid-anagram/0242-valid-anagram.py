class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = True
        if len(s) != len(t):
            res = False
        elif len(s) == len(t):
            for i in s:
                if i not in t:
                    return False
                else:
                    if s.count(i) != t.count(i):
                        return False
        return res