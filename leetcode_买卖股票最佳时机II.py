#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3

思路：
设 tmp 为第 i-1 天卖和 i 天买可以赚取的利润，即 prices[i] - prices[i - 1] ；
当该天利润为正 tmp > 0 ，则将利润加入总利润 profit ；
遍历完成后返回总利润 profit 。
复杂度分析：

时间复杂度 O(N)O(N) ： 只需遍历一次price；
空间复杂度 O(1)O(1) ： 变量使用常数额外空间。

@author: xiaozuo
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

