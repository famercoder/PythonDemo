# 选择排序
def selectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(i+1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [5, 3, 2, 4, 1]
selectionSort(arr)

print(arr)