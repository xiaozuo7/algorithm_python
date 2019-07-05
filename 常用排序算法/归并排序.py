# -*- coding: utf-8 -*-
"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。

该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
1、自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
2、自下而上的迭代；
和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间

复杂度分析： O(nlogn) 辅助空间O(n) 典型的分治法 稳定
@author: xiaozuo
"""

def mergeSort(arr):
    import math
    if len(arr)<2:return arr
    mid = math.floor(len(arr)/2) # 一分为二
    left = arr[0:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res

if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("before:{}".format(list))
    res = mergeSort(list)
    print("after:{}".format(res))