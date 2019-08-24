#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

思路：回溯
@author: xiaozuo
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1 or threshold < 0:
            return 0
        visited = [False] * (rows * cols)
        return self.moving(threshold, rows, cols, 0, 0, visited)

    def moving(self, threshold, rows, cols, curx, cury, visited):
        cnt = 0
        if 0 <= curx < cols and 0 <= cury < rows and not visited[cury * cols + curx]:
            if self.calbitsum(curx) + self.calbitsum(cury) <= threshold:
                visited[cury * cols + curx] = True
                # 能到达格子数为当前位置+四个方向能走到的格子数总和
                cnt = 1 + self.moving(threshold, rows, cols, curx - 1, cury, visited) \
                      + self.moving(threshold, rows, cols, curx, cury - 1, visited) \
                      + self.moving(threshold, rows, cols, curx + 1, cury, visited) \
                      + self.moving(threshold, rows, cols, curx, cury + 1, visited)
        return cnt

    def calbitsum(self, x):
        ressum = 0
        while x != 0:
            ressum += x % 10
            x /= 10
        return ressum