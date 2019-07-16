# -*- coding: utf-8 -*-
"""
插入排序是一种最简单直观的排序算法。

插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。
---------------------
复杂度分析： O(n^2)
@author: xiaozuo
"""

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        preIndex = i-1
        cur = arr[i]
        while preIndex>=0 and arr[preIndex]>cur:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1]=cur
    return arr


if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("before:{}".format(list))
    insertionSort(list)
    print("after:{}".format(list))