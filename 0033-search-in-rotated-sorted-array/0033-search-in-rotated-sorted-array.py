class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found the target
            if nums[mid] == target:
                return mid

            # Check if the LEFT half is sorted
            if nums[left] <= nums[mid]:

                # Is the target inside the sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1      # Search left
                else:
                    left = mid + 1       # Search right

            # Otherwise the RIGHT half must be sorted
            else:

                # Is the target inside the sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1       # Search right
                else:
                    right = mid - 1      # Search left

        return -1
