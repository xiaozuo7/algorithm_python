# -*- coding: utf-8 -*-
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

思路：二分
@author: xiaozuo
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """搜素排序旋转数组"""
        if not nums: return -1

        def half_search(nums, target, l, r):
            """二分查找"""
            mid = (l + r) // 2
            if l > r: return -1
            if nums[mid] == target: return mid
            # 0-mid无旋转
            # 旋转位置到-mid之间 0到旋转位置之间
            if (nums[0] <= target <= nums[mid]) or (target <= nums[mid] < nums[0]) or (nums[mid] < nums[0] <= target):
                return half_search(nums, target, l, mid - 1)
            else:
                return half_search(nums, target, mid + 1, r)

        return half_search(nums, target, 0, len(nums) - 1)

if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2,]
    target = 0
    print(sol.search(nums, target))