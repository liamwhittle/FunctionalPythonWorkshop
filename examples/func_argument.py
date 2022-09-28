import numpy as np
from typing import Callable, List


def merge(a: List, b: List, cmp: Callable) -> List:
    merged_lst = []
    # merge sorted lists until one list is empty
    while len(a) > 0 and len(b) > 0:
        # if b is less than a
        if cmp(a[0], b[0]):
            merged_lst.append(b.pop(0))
        # if a is less than b
        else:
            merged_lst.append(a.pop(0))
    # add the rest of the non empty list
    while len(a) > 0:
        merged_lst.append(a.pop(0))
    while len(b) > 0:
        merged_lst.append(b.pop(0))
    return merged_lst

def mergesort(lst: List, cmp: Callable) -> List:
    """
    :param cmp: function taking two argument, 
    returning true if the first is greater than the second
    """
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if cmp(lst[1], lst[0]):
            return lst
        else:
            return [lst[1], lst[0]]
    else:
        mid = len(lst) // 2
        return merge(mergesort(lst[:mid], cmp), mergesort(lst[mid:], cmp), cmp)

def verbose_comparison(a: int, b: int) -> bool:
    return a > b


nums = [np.random.randint(100) for _ in range(10)]
print(mergesort(nums, verbose_comparison))
print(mergesort(nums, lambda a, b: a > b))
print(mergesort(nums, lambda a, b: a < b))
print(mergesort(nums, lambda a, b: a % 5 > b % 5))
