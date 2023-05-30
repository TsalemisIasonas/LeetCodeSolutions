class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_val = 0
        for i in sentences:
            length = len(i.split(' ')) 
            if length > max_val:
                max_val = length
        return max_val