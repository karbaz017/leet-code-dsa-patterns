def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        print(f"current_sum: {current_sum}")

        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

numbers = [2,7,11,15]
target = 22

result = twoSum(numbers, target)
print(f"result: {result}")
