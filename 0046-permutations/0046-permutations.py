class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def bt(path,used):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    bt(path,used)

                    path.pop()
                    used[i] = False
            
        bt([],[False] * len(nums))
        return ans
