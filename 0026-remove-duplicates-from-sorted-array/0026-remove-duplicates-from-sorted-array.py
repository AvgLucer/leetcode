class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        # if only 1 element
        if len(nums) == 1:
            return 1 
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1