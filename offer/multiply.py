#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法

思路：
B[i]的值可以看作下图的矩阵中每行的乘积。
B[i]的意义是A数组不包括i位置的所有乘积，分为 i左边的元素乘积和 i右边的所有元素乘积。
第一个for计算i左边的乘积，第二个for计算右边的。

设有数组大小为5。
对于第一个for循环
第一步：b[0] = 1;
第二步：b[1] = b[0] * a[0] = a[0]
第三步：b[2] = b[1] * a[1] = a[0] * a[1];
第四步：b[3] = b[2] * a[2] = a[0] * a[1] * a[2];
第五步：b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3];
然后对于第二个for循环
第一步
temp *= a[4] = a[4]; 
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4];
第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3];
第三步
temp *= a[2] = a[4] * a[3] * a[2]; 
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2];
第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1]; 
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1];
@author: xiaozuo
"""

#B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
#从左到右算 B[i]=A[0]*A[1]*...*A[i-1]
#从右到左算B[i]*=A[i+1]*...*A[n-1]
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        num = len(A)
        B = [0]*num
        #B[i]的意义是A数组不包括i位置的所有乘积，分为i左边的元素乘积和 i右边的所有元素乘积。
        #初始化B[0]=1，是因为0左边没有元素，所以乘积为1。
        B[0] = 1
        for i in range(1,num):
            B[i] = B[i-1]*A[i-1]
        temp = 1
        for i in range(num-2,-1,-1):#从后往前遍历不算最后一个（num-1）因为第一个for循环中已经计算了
            temp *= A[i+1]
            B[i] *= temp