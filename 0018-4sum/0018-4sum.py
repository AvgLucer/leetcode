class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final = []
        for no1 in range(len(nums) - 3):
            if no1>0 and nums[no1] == nums[no1 -1]:
                continue
            for no2 in range(no1 + 1,len(nums) -2):
                if no2 > no1 + 1 and nums[no2] == nums[no2-1]:
                    continue
                no3 = no2 + 1
                no4 = len(nums) -1
                while no3 < no4 :
                    total = nums[no1] + nums[no2] + nums[no3] + nums[no4]

                    if total == target:
                        final.append([nums[no1],nums[no2],nums[no3],nums[no4]])
                        no3 +=1
                        no4 -=1
                        while no3 < no4 and nums[no3] == nums[no3 -1]:
                            no3 +=1
                        while no3 < no4 and nums[no4] == nums[no4 +1]:
                            no4 -=1
                                
                    elif total < target :
                        no3 +=1
                    else:
                        no4 -=1
        return final

