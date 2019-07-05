# -*- coding: utf-8 -*-
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

思路：迭代 递归 多元赋值
@author: xiaozuo
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 第一种解法 递归
    def reverseList(self, head):
        if head == None or head.next == None:return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

    # 第二种解法 迭代(用到了python的多元赋值)
    def reverseList_diedai(self, head):
        p = None
        while head:
            head.next, p ,head = p, head, head.next
        return p