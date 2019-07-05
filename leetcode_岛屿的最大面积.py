# -*- coding: utf-8 -*-
"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

思路：
    DFS
    循环扫描网格，碰到0跳过，碰到1就置0并且放入一个记录连续1坐标的列表，然后循环扫描列表，
    每次将被扫描点的四个方向的为1的邻居置0并加入列表。
    列表遍历完毕后其长度就是该岛屿的面积，判断并替换一下最大值就是了。
@author: xiaozuo
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        if len(grid)==0 or len(grid[0])==0:return max_area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                tmp_area = 0
                children = [(i,j)]
                # print(children)
                while children:
                    r, c = children.pop()
                    # print(r,c)
                    if grid[r][c]==0:
                        continue
                    grid[r][c]=0 # 置为0
                    tmp_area += 1
                    if r-1>=0 and grid[r-1][c]:
                        children.append((r-1, c))
                    if r+1<len(grid) and grid[r+1][c]:
                        children.append((r+1, c))
                    if c-1>=0 and grid[r][c-1]:
                        children.append((r, c-1))
                    if c+1<len(grid[0]) and grid[r][c+1]:
                        children.append((r, c+1))
                max_area = max(max_area, tmp_area)
        return max_area

if __name__=='__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid=grid))