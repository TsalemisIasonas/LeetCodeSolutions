class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        count_a = 0
        count_b = 0
        for i in a:
            if i in vowels:
                count_a +=1
        for j in b:
            if j in vowels:
                count_b +=1
        return count_a == count_b