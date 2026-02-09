class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        left = 0
        right = len(nums) - 1

        result = [0] * len(nums)

        index = len(nums) - 1

        while index >= 0:
            if nums[left] > nums[right]:
                result[index] = nums[left]
                left += 1
                index -= 1
            else:
                result[index] = nums[right]
                right -= 1
                index -= 1

        return result
