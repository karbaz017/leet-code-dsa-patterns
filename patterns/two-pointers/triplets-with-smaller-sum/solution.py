class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        arr.sort()

        current_sum = arr[0] + arr[1] + arr[2]

        count = 0

        for i in range(n):
            left = i + 1
            right = n - 1
            
            while left < right:
                
                current_sum = arr[i] + arr[left] + arr[right]
                    
                if current_sum < sum:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count
