#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

思路：借助辅助栈 比较stack[-1] 和 popV[0] 相等就抵消 直到全部消除
@author: xiaozuo
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV or len(pushV) != len(popV):return False
        stack = []
        while popV:
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    pushV = [1,2,3,4,5]
    popV = [4,3,5,1,2]
    print(sol.IsPopOrder(pushV=pushV, popV=popV))