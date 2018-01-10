def bubble_sort(arr):
    n = len(arr)                   #获得数组的长度
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:       #如果前者比后者大
                arr[j-1], arr[j] = arr[j], arr[j-1]      #则交换两者
    return arr

alist = [54,26,93,17,77,31,44,55,60]
print(bubble_sort(alist))
