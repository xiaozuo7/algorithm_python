# -*- coding: utf-8 -*-
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

思路： 排序 回溯 一次遍历
@author: xiaozuo
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 排序
        n = len(nums)
        res = [[]]
        for i in range(n-1,-1,-1):
            for tmp in res[:]:
                res.append(tmp+[nums[i]])
                if res.count(res[-1])>1:  # 去重
                    res.pop()
        return res