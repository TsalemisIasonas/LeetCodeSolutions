class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for i in s:
            if i not in visited:
                visited.add(i)
            else:
                return i
            