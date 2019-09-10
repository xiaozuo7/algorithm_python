#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

思路：简单介绍一下,如果一个数组为[a1, a2, a3, a4, a5],

a5 - a1 = (a2 - a1) + (a3 - a2) + (a4 - a3) + (a5 - a4)

所以,我们这一题就是找两个差值最大数!

@author: xiaozuo
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_max = 0
        for i in range(1, len(prices)):
            # 记录目前位置以i为结束的, 差值最大值
            cur_max += (prices[i] - prices[i-1])
            # 如果 cur_max 小于0 说明要改变起始的位置
            cur_max = max(0, cur_max)
            res = max(res, cur_max)
        return res

class DP:
    def maxProfit(self, prices: List[int]) -> int:
        """动态规划"""
        if not prices: return 0
        res = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return res

