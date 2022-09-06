from typing import List


def pivotIndex(nums: List[int]) -> int:
    s = sum(nums)
    for i in range(len(nums)):
        sumL = sum(nums[:i])
        if s-sumL-nums[i] == sumL:
            return i
    return -1