#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路：
如果一个整数不为0，那么这个整数至少有一位是1。
如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，
原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。
其余所有位将不会受到影响。
把原来的整数和减去1之后的结果做  与  运算，从原来整数最右边一个1那一位开始所有位都会变成0
举例来说，6的二进制是 110 ，6-1=5的二进制是 101，6&5=100， 如此操作之后6中原来的110变为100，循环计数统计1的个数，直至n变为0为止。

python2 分int32 和 int 64
python3 超过32和64后, 自动转型为长整形, 长整形理论上没有限制
@author: xiaozuo
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n-1)
        return count

    def NumberOf1_bin(self, n):
        return bin(n & 0xffffffff).count('1')

if __name__ == '__main__':
    sol = Solution()
    n = 6
    print(sol.NumberOf1(n=n))
    print(sol.NumberOf1_bin(n=n))