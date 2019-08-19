#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：为了当最小元素被找到后，如果恰好最小元素在栈顶被弹出，
那么还可以接着寻找次小元素，因此定义一个辅助栈，每次往数据栈中压入元素的时候，也都把最小的元素压入辅助栈，
这样就能保住辅助栈的栈顶一直都是最小的元素。当最小的元素从数据栈中弹出后，同时弹出辅助栈里的最小元素，这样辅助栈的栈顶元素就是下一个最小值。


@author: xiaozuo
"""
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self):
        # write code here
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]

