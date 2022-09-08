from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    if target < nums[0]:
        return 0
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] < target and (i+1 < len(nums) and nums[i+1] > target):
            return i + 1
    return len(nums)