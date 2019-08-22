#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

思路：hash  异或   0 ^= i
@author: xiaozuo
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        """一个整数数组出现一次的两个数，其余两次"""
        # write code here
        d = {}
        for i in array:
            try:
                d.pop(i)
            except:
                d[i] = 1
        res = []
        for k in d.keys():
            res.append(k)
        return res