class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(' ')
        words = [i[0].upper() + i[1:].lower() for i in words]
        res = []
        for i in words:
            if len(i) <= 2 : res.append(i.lower())
            else: res.append(i)
        return ' '.join(res)