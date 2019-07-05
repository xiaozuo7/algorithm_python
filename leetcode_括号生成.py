# -*- coding: utf-8 -*-
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

思路：  回溯 如果有位置放左括号就放，如果放有括号的剩余位置大于左括号，就放右括号。

@author: xiaozuo
"""

class Solution:
    def generateParenthesis(self, n):
        res = []
        self.backtrack(n, n, '', res)
        return res

    def backtrack(self, left, right, tmp, res):
        if left==0 and right==0:
            res.append(tmp)
            return
        if left>0:
            self.backtrack(left-1, right, tmp+'(', res)
        if right>left:
            self.backtrack(left, right-1, tmp+')', res)

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(n=3))