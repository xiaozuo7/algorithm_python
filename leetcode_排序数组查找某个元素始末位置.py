# -*- coding: utf-8 -*-
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

思路：两次二分法 双指针
@author: xiaozuo
"""


class Solution:
    def searchRange(self, nums, target):
        """排序数组查找某个元素始末位置"""
        left = self.help(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, self.help(nums, target, False) - 1]

    def help(self, nums, target, vis):
        """vis判断递归哪个区间"""
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (vis and target == nums[mid]):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    sol = Solution()
    nums = [5,6,7,7,8,9]
    target = 7
    print(sol.searchRange(nums, target))