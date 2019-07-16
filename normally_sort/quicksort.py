# -*- coding: utf-8 -*-
"""

@author: xiaozuo
"""

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        provit = arr[0]
        less = [i for i in arr[1:] if i <= provit]
        greater = [i for i in arr[1:] if i > provit]
    return quicksort(less) + [provit] + quicksort(greater)

if __name__ == '__main__':
    arr = [1,5,2,87,4,9]
    print(quicksort(arr=arr))