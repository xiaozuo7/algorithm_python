#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

思路：
动态规划方程： f(i)=nums[i]+max{f(i−1),0}
如果加入一个树之后为负数，那就直接从这个数开始重新计算
@author: xiaozuo
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)