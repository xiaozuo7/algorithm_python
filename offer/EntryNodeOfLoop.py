#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

思路：快慢指针
@author: xiaozuo
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        """链表中环的入口结点"""
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow = pHead.next
        fast = slow.next
        # 找到相遇点
        while fast != slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            # 慢指针回到表头，快指针留在相遇点，二者同步往前直到相遇在入口结点
            slow = pHead
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow
        return None