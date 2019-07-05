# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort() # 排序 必须
        n = len(nums)
        res = float("inf") # 正无穷大
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == target: return target
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,-2,3,7]
    target = 1
    print(sol.threeSumClosest(nums=nums, target=target))