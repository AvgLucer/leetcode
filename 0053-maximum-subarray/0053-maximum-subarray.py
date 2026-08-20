class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur  = nums[0]
        for x in nums[1:]:
            cur = max(x,cur + x)
            ans = max(ans,cur)
        return ans
        
