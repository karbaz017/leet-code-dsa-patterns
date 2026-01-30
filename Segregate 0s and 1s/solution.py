def segregate0and1(arr):
    left = 0
    right = len(arr) - 1

    print(f"arr: {arr}")

    while left < right:
        print(f"left: {left} right: {right}")
        if arr[left] == 0 and arr[right] == 1:
            print("Inside 1st vlock")
            left += 1
            right -= 1
        
        elif arr[left] == 1 and arr[right] == 0:
            print("Inside 2nd vlock")
            arr[left] = 0
            arr[right] = 1

            left += 1
            right -= 1

        elif arr[left] == 0 and arr[right] == 0:
            print("Inside 3rd vlock")
            left += 1
        
        elif arr[left] == 1 and arr[right] == 1:
            print("Inside 4th vlock")
            right -= 1

        print(f"left: {left} right: {right} arr: {arr}")
        print("####################################")
        
    return arr

print(f"{segregate0and1([0, 0, 1, 1, 0])}")