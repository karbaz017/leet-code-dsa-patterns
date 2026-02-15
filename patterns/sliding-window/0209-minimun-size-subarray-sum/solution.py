class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        min_len = float('inf')
        sum = 0

        while high < len(nums):
            sum += nums[high] # 2, 5, 6,  10

            while sum >= target and low <= high:
                if min_len > high - low + 1:
                    min_len = high - low + 1 # 4
                sum -= nums[low] # 6
                low += 1

            high += 1 # 3, 4

        if min_len == float('inf'):
            min_len = 0

        return min_len
