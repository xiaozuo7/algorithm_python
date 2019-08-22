#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
整数中1出现的次数

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

思路：
将n的各个位分为两类：个位与其它位。
对个位来说：

若个位大于0，1出现的次数为round*1+1
若个位等于0，1出现的次数为round*1
对其它位来说，记每一位的权值为base，位值为weight，该位之前的数是former，

n = 534   对于3来说
round =5 weight=3 former=4 base = 10

若weight为0，则1出现次数为round*base
若weight为1，则1出现次数为round*base+former+1
若weight大于1，则1出现次数为round*base+base

534 = （个位1出现次数）+（十位1出现次数）+（百位1出现次数）=（53*1+1）+（5*10+10）+（0*100+100）= 214
530 = （53*1）+（5*10+10）+（0*100+100） = 213
504 = （50*1+1）+（5*10）+（0*100+100） = 201
514 = （51*1+1）+（5*10+4+1）+（0*100+100） = 207
10 = (1*1)+(0*10+0+1) = 2

@author: xiaozuo
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        count = 0
        base = 1
        round = n
        while round > 0:
            weight = round % 10
            # print("weight:{}".format(weight))
            round = round // 10
            # print("round:{}".format(round))
            count += round * base
            if weight == 1:
                count += (n % base) + 1
            elif weight > 1:
                count += base
            base *= 10
        return count

if __name__ == '__main__':
    sol = Solution()
    n = 514
    print(sol.NumberOf1Between1AndN_Solution(n=n))