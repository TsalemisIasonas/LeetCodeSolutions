class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        new = [''] * len(words)
        for i in words:
            new[int(i[-1])-1] = i[:-1]
        output = ' '.join(new)
        return output


