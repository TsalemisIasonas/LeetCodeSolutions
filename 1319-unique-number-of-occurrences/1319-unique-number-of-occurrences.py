class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        return len(set(freq_map.values())) == len(freq_map)
            