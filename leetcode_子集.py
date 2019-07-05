# -*- coding: utf-8 -*-
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

思路： 回溯 一次遍历
@author: xiaozuo
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for i in range(n-1,-1,-1):
            for tmp in res[:]:
                res.append(tmp+[nums[i]])
        return res