#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
heapq库函数
@author: xiaozuo
"""
"""创建堆1"""
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


"""创建堆2"""
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]

"""merge"""
import heapq

num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)
print(list(res))

"""弹出最小值 heappop()"""
import heapq
nums = [2, 43, 45, 23, 12]
heapq.heapify(nums)

print(heapq.heappop(nums))
# out: 2

"""如果需要所有堆排序后的元素"""
result = [heapq.heappop(nums) for _ in range(len(nums))]
print(result)
# out: [12, 23, 43, 45]


"""代替最小元素"""
import heapq

nums = [1, 2, 4, 5, 3]
heapq.heapify(nums)

heapq.heapreplace(nums, 23)

print([heapq.heappop(nums) for _ in range(len(nums))])
# out: [2, 3, 4, 5, 23]

"""获取最小最大值"""
import heapq

nums = [1, 3, 4, 5, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

"""
输出：
[5, 4, 3]
[1, 2, 3]
"""