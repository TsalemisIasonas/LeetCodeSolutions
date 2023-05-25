class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [chr(i) for i in range(97,123)]
        return all(char in sentence for char in alphabet)
