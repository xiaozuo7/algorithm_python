# -*- coding: utf-8 -*-
"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

思路：排序找中位数 摩尔投票
@author: xiaozuo
"""
class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) // 2]


    # 摩尔投票法
    def mole(self, nums):
        tmp = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                tmp = nums[i]
            if nums[i]==tmp:
                count += 1
            else:
                count -= 1
        return tmp