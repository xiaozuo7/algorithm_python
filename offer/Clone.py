#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

复制一个复杂链表  每个结点不仅指向下一结点 还指向一个随机结点
@author: xiaozuo
"""
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:return pHead
        copy_p = RandomListNode(pHead.label)
        copy_p.random = pHead.random
        copy_p.next = self.Clone(pHead.next)
        return copy_p