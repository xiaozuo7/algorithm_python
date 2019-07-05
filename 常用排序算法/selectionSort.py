# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""

def findSmallest(arr):
    """存储最小的值"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """选择排序"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    arr = [5,2,1,8,4,9]
    print(selectionSort(arr=arr))
