class Solution:
    def isPalindrome(self, s: str) -> bool:
        strChars = [i for i in s.lower() if i.isalnum()]
        strCharsReversed = [i for i in strChars]
        strChars.reverse()
        print(strChars,strCharsReversed)
        return all(strChars[i] == strCharsReversed[i] for i in range(len(strChars)))