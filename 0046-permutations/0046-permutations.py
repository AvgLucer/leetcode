class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        if len(nums) == 1:
            return [nums]
        
        ans = []

        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i+1:]):
                ans.append([nums[i]] + p)
        return ans
        