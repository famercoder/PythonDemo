def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr = [1, 2, 3, 4, 5]
index = binarySearch(arr, 2)

print(index)