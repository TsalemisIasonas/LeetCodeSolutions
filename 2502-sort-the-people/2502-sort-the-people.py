class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        struct = dict(zip(heights, names))
        new_struct = {k: struct[k] for k in sorted(struct, reverse = True)}
        return list(new_struct.values())


            
        