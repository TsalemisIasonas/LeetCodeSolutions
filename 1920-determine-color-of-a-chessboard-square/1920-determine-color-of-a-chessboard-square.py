class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col_one = ['a','c','e','g']
        col_two = ['b','d','f','h']
        letter = coordinates[0]
        num = int(coordinates[-1])
        if letter in col_one:
            if num%2 == 0:
                return True
            else:
                return False
        else:
            if num%2 == 0:
                return False
            else:
                return True