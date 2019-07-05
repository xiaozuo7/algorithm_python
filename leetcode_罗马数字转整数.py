# -*- coding: utf-8 -*-
"""
按顺序读取罗马数字，当前数字小于下一个数字，则是下一个数字减去当前数字，否则直接相加

比如IV就是*-1+5=4*，而IIV这种情况是不存在的，对于其他量级的数字也是同理。

实际处理的时候最后一个数字无法和它下一个数字比较，因为不存在下一个数字。

但是最后一个数字永远是加的而不是减的，所以就单独拎出来处理就好。
@author: xiaozuo
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans = 0
        for i, char in enumerate(s[:-1]):
            if dic[char] >= dic[s[i+1]]: #最后一位数字无法比较因为最后一位数字永远是加
                ans += dic[char]
            else:
                ans -= dic[char]
        ans += dic[s[-1]]
        return ans