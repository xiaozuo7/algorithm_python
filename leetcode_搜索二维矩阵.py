# -*- coding: utf-8 -*-
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

思路：二分法，二维合成一维，找到相应变化的坐标
@author: xiaozuo
"""

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:return False
        n = len(matrix[0])
        left = 0
        right = n*m-1
        while left<=right:
            mid = (left+right)//2
            coor = matrix[mid//n][mid%n] # row=[mid//n] col=[mid%n]
            if target == coor:
                return True
            else:
                if target<coor:
                    right = mid-1
                else:
                    left = mid+1
        return False