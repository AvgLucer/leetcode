class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
                old_max = max_prod
                old_min = min_prod
                max_prod = max(nums[i] * old_max  , nums[i] * old_min , nums[i] )
                min_prod = min(nums[i] * old_max  , nums[i] * old_min , nums[i])

                answer = max(max_prod,answer)

        return answer

