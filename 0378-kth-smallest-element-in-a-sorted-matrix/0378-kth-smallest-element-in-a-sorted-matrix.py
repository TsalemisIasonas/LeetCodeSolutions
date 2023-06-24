class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elements = [j for i in matrix for j in i]
        return sorted(elements)[k-1]