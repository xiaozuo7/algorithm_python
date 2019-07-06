# -*- coding: utf-8 -*-
"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
@author: xiaozuo
"""

class Solution:
    """二维数组查找target"""
    def Find(self, target, array):
        # write code here
        if len(array)<1 or len(array[0])<1:return False
        n = len(array)
        for i in range(n):
            for j in range(len(array[0])):
                k = array[i][-j]
                if k != target:
                    j += 1
                if k == target:
                    return True
        return False