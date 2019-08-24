#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


思路：利用递归，如果当前节点是重复节点时，越过与当前节点相同的节点，
找到第一个与当前节点的值不相同的节点，
从第一个与当前结点不同的结点开始递归（重复的节点一个都不留）。
如果当前节点不是重复节点，保留当前节点，从下一个节点开始递归。
@author: xiaozuo
"""
class Solution:
    def deleteDuplication(self, pHead):
        """删除链表中重复的结点"""
        # write code here
        if not pHead:return None
        if pHead.next == None:return pHead
        while pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead # 后面的节点递归结束后，返回pHead即可
        else:
            dummy = pHead
            while dummy and dummy.val == pHead.val:
                dummy = dummy.next
            # 重复节点都不留，不保留pHead，直接返回下一个不同节点的递归结点。
            return self.deleteDuplication(dummy)