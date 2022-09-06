from typing import List
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums3 = sorted(nums1 + nums2)
    median = 0
    if len(nums3)%2 == 0:
        median = (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2)-1])/2
    else:
        median = nums3[int(len(nums3)/2)]
    return median