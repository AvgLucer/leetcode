class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0 
        for j in range(0,len(nums)):
            if val != nums[j]:
                nums[i] = nums[j]
                i += 1
            
        return i
