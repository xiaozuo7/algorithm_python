#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
@author: xiaozuo
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2 == []:
            while self.stack1:
                num = self.stack1.pop()
                self.stack2.append(num)
        return self.stack2.pop()