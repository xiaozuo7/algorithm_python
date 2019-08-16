#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:return 0
        n = len(rotateArray)
        l = 0
        r = n-1
        while r-l > 1:
            mid = (l+r)//2
            # 考虑[1,0,1,1,1]的情况
            if rotateArray[l] == rotateArray[r] == rotateArray[mid]:
                for i in range(l+1, r+1):
                    if rotateArray[i] < rotateArray[l]:
                        return rotateArray[i]
            elif rotateArray[mid] >= rotateArray[l]:
                l = mid
            elif rotateArray[mid] <= rotateArray[r]:
                r = mid
        return rotateArray[r]

if __name__ == '__main__':
    sol = Solution()
    arr = [3,4,5,1,2]
    print(sol.minNumberInRotateArray(rotateArray=arr))