class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return len(set(freq.values())) == 1