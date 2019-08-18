#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

思路：每次打印第一行 然后逆时针旋转90度
@author: xiaozuo
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        """逆时针旋转90度"""
        row = len(matrix)
        col = len(matrix[0])
        new_matrix = []
        for i in range(col):
            tmp = []
            for j in range(row):
                tmp.append(matrix[j][i])
                # print(tmp)
            new_matrix.append(tmp)
        new_matrix.reverse()
        return new_matrix

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14 ,15, 16]]
    print(sol.printMatrix(matrix=matrix))