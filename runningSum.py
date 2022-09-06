from typing import List


def runningSum(nums: List[int]) -> List[int]:
    ansList = []
    sum = 0
    for i in nums:
        ansList.append(i+sum)
        sum += i
    return ansList