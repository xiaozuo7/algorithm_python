#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。

简要描述：抽五张牌  大小王任意替换 时顺子就True

思路： 排序，算间隙gap 统计大小王的个数  判断是否够补
@author: xiaozuo
"""
class Solution:
    def IsContinuous(self, numbers):
        """扑克牌顺子"""
        # write code here
        if not numbers:return False
        numbers.sort()
        index = numbers.count(0)
        gap = 0
        l = index
        r = index + 1
        while r < len(numbers):
            if numbers[l] == numbers[r]:
                return False
            gap += numbers[r] - numbers[l] - 1
            l = r
            r += 1
        return gap <= index

if __name__ == '__main__':
    sol = Solution()
    numbers = [1,0,3,0,5]
    print(sol.IsContinuous(numbers=numbers))