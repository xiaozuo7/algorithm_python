#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

思路：快排
@author: xiaozuo
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k < 0 or not tinput:
            return []
        # import heapq
        # return heapq.nsmallest(k, arr)

        res = self.quicksort(tinput)
        return res[:k]
    def quicksort(self, arr):
        if len(arr) < 2:
            return arr
        else:
            provit = arr[0]
            less = [i for i in arr[1:] if i <= provit]
            greater = [i for i in arr[1:] if i > provit]
        return self.quicksort(less) + [provit] + self.quicksort(greater)

if __name__ == '__main__':
    sol = Solution()
    tinput = [1,2,5,6,3,4,8,7]
    k = 4
    print(sol.GetLeastNumbers_Solution(tinput=tinput, k = k))