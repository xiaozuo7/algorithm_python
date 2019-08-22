#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入两个链表，找出它们的第一个公共结点。

思路：最简单的就是数组存储值并查找  也可以一起两个指针搜索
@author: xiaozuo
"""
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """两个链表的第一个公共结点"""

        # l1 = pHead1
        # l2 = pHead2
        # while l1 != l2:
            # l1 = l1.next if l1 else pHead2
            # l2 = l2.next if l2 else pHead1
        # return l1

        res = []
        while pHead1:
            res.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in res:
                return pHead2
            pHead2 = pHead2.next