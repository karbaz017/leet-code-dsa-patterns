class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k - 1

        sum = 0
        for i in range(low, high + 1):
            sum += arr[i]

        max_sum = sum 

        low += 1
        high = low + k - 1

        while high < len(arr):
            sum = sum - arr[low-1]
            sum = sum + arr[high]
            
            if sum > max_sum:
                max_sum = sum
            
            low += 1
            high += 1

        return max_sum
