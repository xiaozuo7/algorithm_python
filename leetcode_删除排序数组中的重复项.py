# -*- coding: utf-8 -*-
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
@author: xiaozuo
"""

class Solution:
    """删除排序数组中的重复项"""
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1 if nums else 0

if __name__ == '__main__':
    nums = [0,0,0,0,0]
    sol = Solution()
    print(sol.removeDuplicates(nums))