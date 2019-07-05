# -*- coding: utf-8 -*-
"""
希尔排序（shell sort）这个排序方法又称为缩小增量排序，是1959年D·L·Shell提出来的。
该方法的基本思想是：设待排序元素序列有n个元素，首先取一个整数increment（小于n）作为间隔将全部元素分为increment个子序列，
所有距离为increment的元素放在同一个子序列中，在每一个子序列中分别实行直接插入排序。
然后缩小间隔increment，重复上述子序列划分和排序工作。直到最后取increment=1，将所有元素放在同一个子序列中排序为止。

由于开始时，increment的取值较大，每个子序列中的元素较少，排序速度较快，
到排序后期increment取值逐渐变小，子序列中元素个数逐渐增多，但由于前面工作的基础，大多数元素已经基本有序，所以排序速度仍然很快。

第一趟取increment的方法是：n/3向下取整+1=3（关于increment的取法之后会有介绍）。将整个数据列划分为间隔为3的3个子序列，
    然后对每一个子序列执行直接插入排序，相当于对整个序列执行了部分排序调整。
第二趟将间隔increment= increment/3向下取整+1=2，将整个元素序列划分为2个间隔为2的子序列，分别进行排序
第三趟把间隔缩小为increment= increment/3向下取整+1=1，当增量为1的时候，实际上就是把整个数列作为一个子序列进行插入排序

复杂度分析： O(nlogn)~O(n^2)  最好： O(n^1.3)  不稳定
@author: xiaozuo
"""

def shellSort(arr):
    import math
    gap = 1  # 增量
    n = len(arr)
    while gap < (n/3):
        gap = gap*3+1
    while gap>0:
        for i in range(gap, n):
            temp = arr[i]
            j = i-gap
            while j>=0 and arr[j]>temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("before:{}".format(list))
    shellSort(list)
    print("after:{}".format(list))