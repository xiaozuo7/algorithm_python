# -*- coding: utf-8 -*-
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai)
。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

思路： 双指针
@author: xiaozuo
"""

class Solution:
    def maxArea(self, height) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l < r:
            res = max(res, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    h = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height=h))