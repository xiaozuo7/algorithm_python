# -*- coding: utf-8 -*-
"""
约瑟夫环的最简单做法
例题：问一个监狱有100名犯人准备枪毙, 枪毙之前让他们报数, 如果报的单数, 就枪毙, 如果是双数, 就留下,
剩下的人继续依次进行下一轮报数, 直到剩下最后一人就释放, 问如果想活命, 一开始应该站哪个位置
@author: xiaozuo
"""

def getIndex(divide, scale, max_num):
    '''

    :param divide:  他是起始被计算的数, 之后的每次都不同, 第一次它应该是1
    :param scale:  进制数, 按该数进行区分
    :param max_num: 给出的最大数, 需要计算的范围
    :return:  在max_num中存的最大进制数
    '''
    divide *= scale
    return divide if divide * scale >= max_num else getIndex(divide, scale, max_num)
print(getIndex(1,2,100))