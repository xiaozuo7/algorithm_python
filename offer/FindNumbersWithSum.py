#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

@author: xiaozuo
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """和为S的两个数字"""
        # write code here
        l = 0
        r = len(array) - 1
        while l < r:
            left = array[l]
            right = array[r]
            if left + right == tsum:
                return (left, right)
            elif left + right > tsum:
                r -= 1
            else:
                l += 1
        return []

if __name__ == '__main__':
    sol = Solution()
    array = [1, 2, 3, 4, 5, 7, 15]
    print(sol.FindNumbersWithSum(array=array, tsum=9))