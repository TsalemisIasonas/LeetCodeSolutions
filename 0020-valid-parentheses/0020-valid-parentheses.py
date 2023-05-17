class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        slist = []

        for i in s:
            if i in valid.keys():
                slist.append(i)
            elif i in valid.values() and slist:
                if valid[slist[-1]] == i:
                    slist.pop()
                else:
                    return False
            else:
                return False

        return not slist
