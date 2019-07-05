# -*- coding: utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true

思路：压栈，与栈顶元素进行匹配
@author: xiaozuo
"""

class Solution:
    def isValid(self, s):
        stack = []
        lookup = {"(":")",
                  "[":"]",
                  "{":"}"
                  }
        for alp in s:
            if alp in lookup:
                stack.append(alp)
                continue
            if stack and lookup[stack[-1]]==alp:
                stack.pop()
            else:
                return False
        return True if not stack else False

if __name__ == '__main__':
    sol=Solution()
    s = "{[()]}"
    print(sol.isValid(s=s))