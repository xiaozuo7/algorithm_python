#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

统计一个数字在排序数组中出现的次数。
@author: xiaozuo
"""
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        import collections
        d = collections.Counter(data)
        for key, value in d.items():
            if key == k:
                return value
        return 0