from typing import List


def merge_sorting(lst: List[int]):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sorting(lst[:mid])
    right = merge_sorting(lst[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
    else:
        result.append(right[j])
        j += 1
        return result + left[i:] + right[j:]
