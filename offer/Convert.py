#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


思路：中序遍历
Head用于记录链表的头节点，用于最后算法的返回；listTail用于定位当前需要更改指向的节点。
@author: xiaozuo
"""
class Solution:
    def __init__(self):
        self.head = None   # Head用于记录链表的头节点，用于最后算法的返回
        self.tail = None   # Tail用于定位当前需要更改指向的节点。
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return
        self.Convert(pRootOfTree.left)  # 中序遍历

        # 中序遍历到第一个节点时调用，自此之后Head不变，Tail跟随算法的进度
        if self.head == None:
            self.head = pRootOfTree
            self.tail = pRootOfTree
        else:
            self.tail.right, pRootOfTree.left, self.tail = pRootOfTree, self.tail, pRootOfTree # 改变tail指向
        self.Convert(pRootOfTree.right)  # 中序遍历
        return self.head
