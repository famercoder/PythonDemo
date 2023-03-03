def quickSort(arr):
    if len(arr) <= 1:
        return arr

    privot = arr[0]
    lessArr = [i for i in arr[1:] if i <= privot]
    greaterArr = [i for i in arr[1:] if i > privot]
    return quickSort(lessArr) + [privot] + quickSort(greaterArr)

arr = quickSort([1, 3, 2, 5, 4])
print(arr)