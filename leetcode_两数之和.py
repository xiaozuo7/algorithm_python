# -*- coding: utf-8 -*-
"""
两数之和 哈希（在python中叫做字典）

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
@author: xiaozuo
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = {}  # 创建一个空字典
        for x in range(n):
            a = target - nums[x]  # a为差值 也是字典的key
            if nums[x] in d:  # 如果字典中存在num[x]则返回字典的值
                return d[nums[x]], x
            else:
                d[a] = x

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print('{}'.format(result))