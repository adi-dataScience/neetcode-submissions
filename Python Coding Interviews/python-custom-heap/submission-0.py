import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    nums1=[]
    for i in nums:
        heapq.heappush(nums1,(-i,i))

    result=[]
    for i in range(len(nums1)):
        new=heapq.heappop(nums1)
        result.append(new[1])
    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
