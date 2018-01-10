def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用 round 四舍五入取整
    while gap > 0:
        for i in range(gap, n):        #每一列进行插入排序 , 从 gap 到 n-1
            temp = ary[i]
            j = i
            while (j>=gap and ary[j-gap]>temp):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        print(ary)
        gap = round(gap/2)                     #重新设置步长
    return ary


alist = [7,6,4,3,1,2,8]
print(shell_sort(alist))
