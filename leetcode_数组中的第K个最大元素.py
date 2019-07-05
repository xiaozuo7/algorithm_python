# -*- coding: utf-8 -*-
"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

思路： 快排
@author: xiaozuo
"""

class Solution:
    def findKthLargest(self, nums, k):
        """单纯的快排"""
        self.nums = nums
        self.quickSort(nums, 0, len(nums)-1)
        return nums[-k]

    def quickSort(self, nums, start, end):
        """快排"""
        if start < end:
            i, j = start, end
            base = nums[i]
            while i<j:
                while i<j and nums[j] >= base:
                    j -= 1
                nums[i] = nums[j]
                while i<j and nums[i] <= base:
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            self.quickSort(nums, start,i-1)
            self.quickSort(nums, j+1, end)
        return nums

    def findKthLargest1(self, nums, k):
        """借助快排的思想"""
        l = [x for x in nums if x>nums[0]]
        m = [x for x in nums if x==nums[0]]
        r = [x for x in nums if x<nums[0]]
        f = self.findKthLargest1

        if k<=len(l):
            return f(l, k)
        elif k<=len(l)+len(m):
            return nums[0]
        return f(r, k-len(l)-len(m))


if __name__ == '__main__':
    sol = Solution()
    import numpy as np
    nums = np.random.randint(10,size=10)
    print(nums)
    print(sol.findKthLargest(nums, k=4))
    print(sol.findKthLargest1(nums, k=4))