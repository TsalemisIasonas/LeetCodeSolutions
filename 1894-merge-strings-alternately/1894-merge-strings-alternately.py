class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        length = min(len(word1),len(word2))
        for i in range(length):
            res+=word1[i]
            res+=word2[i]
        if length == len(word1):
            for i in range(length,len(word2)):
                res+=word2[i]
        else:
            for i in range(length,len(word1)):
                res+=word1[i]

        return res