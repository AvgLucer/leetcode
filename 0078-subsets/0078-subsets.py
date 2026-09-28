class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for num in nums:
            res += [x + [num] for x in res]
        
        return res
