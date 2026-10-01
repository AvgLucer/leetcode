class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        prefix= 1
        #left Products
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]
        suffix=1
        #right products
        for i in range(n-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
