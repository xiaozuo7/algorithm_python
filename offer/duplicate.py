#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。

思路：
于数组中元素都在0~n - 1的范围内，如果这个数组中没有重复元素，那么当数组排序后，
数字i将会处于i的位置。
从头到尾依次扫描数组中的元素，当扫描第i个元素时，如果这个元素是i，则继续扫描下一个元素，
如果不是i，而是m，则将其与第m个元素比较，如果两者相等，则找到了重复的数字，
如果不相等，则将二者交换位置，
重复该过程，直到找到重复元素。
时间复杂度O(n)，空间复杂度O(1).
@author: xiaozuo
"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numbers.sort()  # 排序
        for i in range(len(numbers)):
            while numbers[i] != i: # 当值与序列号不一致时
                if numbers[numbers[i]] == numbers[i]: # 比较当前数与前一个数是否相等
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]] # 交换数字使numbers[i]按顺序排列
        return False