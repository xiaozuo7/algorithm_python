#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


思路：
1.二叉树为空，则返回空；

2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；

3.节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
@author: xiaozuo
"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode: return None  # 空树
        if pNode.right:                   # 节点右孩子存在
            pNode = pNode.right           # 节点从右孩子出发
            while pNode.left:             # 找左子节点指针
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:        # 节点是左孩子
                if pNode == pNode.next.left:  # 返回父节点
                    return pNode.next
                pNode = pNode.next # 向上遍历父节点的父节点
        return None
