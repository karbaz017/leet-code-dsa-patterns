class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 1
        while k < len(nums):
            if nums[i] != nums[k]:
                i += 1
                nums[i] = nums[k]
            else:
                k += 1
        
        return i + 1