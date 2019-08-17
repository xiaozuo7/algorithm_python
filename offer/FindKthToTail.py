#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个链表，输出该链表中倒数第k个结点

思路一：快慢指针
思路二：stack直接添加
@author: xiaozuo
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k < 1: return None
        fast = head
        slow = head
        for _ in range(k - 1):
            fast = fast.next
            if fast == None:
                return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow


    # if not head or k<1:
    #     return None
    # stack = []
    # cur = head
    # while cur:
    #     stack.append(cur)
    #     cur = cur.next
    # if k > len(stack):
    #     return None
    # return stack[-k]