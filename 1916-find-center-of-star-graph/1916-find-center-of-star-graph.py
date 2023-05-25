class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        target = 0
        for i in edges[0]:
            for j in edges[1]:
                if i == j:
                    target = i
                    break
        return target