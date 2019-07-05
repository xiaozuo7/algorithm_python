# -*- coding: utf-8 -*-
"""
选择排序是一种简单直观的排序算法。

无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

复杂度： O(n²)
@author: xiaozuo
"""

class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j]<arr[minIndex]:
                    minIndex = j
            if i!=minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

if __name__ == '__main__':
    sol = Solution()
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print(sol.selectionSort(arr=list))