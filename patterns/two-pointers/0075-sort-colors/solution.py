class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        left = 0
        mid = 0
        right = n

        while mid <= right:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[left]
                nums[left] = temp

                mid += 1
                left += 1
            elif nums[mid] == 2:
                temp = nums[right]
                nums[right] = nums[mid]
                nums[mid] = temp

                right -= 1
            else:
                mid += 1
