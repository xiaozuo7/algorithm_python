#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


思路：滑动窗口
@author: xiaozuo
"""
class Solution:
    def maxInWindows(self, num, size):
        """滑动窗口的最大值"""
        # write code here
        if not num or not size:return []
        l = 0
        r = size
        res = []
        while r <= len(num):
            cur = max(num[l:r])
            res.append(cur)
            l += 1
            r += 1
        return res