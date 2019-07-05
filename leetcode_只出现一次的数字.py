# -*- coding: utf-8 -*-
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

示例 2:

输入: [4,1,2,1,2]
输出: 4

方法： 异或运算  hash O(n)
@author: xiaozuo
"""

class Solution:
    def singleNumber(self, nums):
        res = 0
        for tmp in nums:
            res ^= tmp
        return res

    # hash表做法
    def hash(self, nums):
        d = {}
        for tmp in nums:
            try:
                d.pop(tmp)
            except:
                d[tmp]=1
        return d.popitem()[0]

if __name__ == '__main__':
    sol=Solution()
    nums = [4,1,2,1,2]
    print(sol.singleNumber(nums))
    print(sol.hash(nums))