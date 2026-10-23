import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    
    negated=[]
    for i in nums:
        heapq.heappush(negated,-i)
    
    result=[]
    for i in range(len(negated)):
        new=-heapq.heappop(negated)
        result.append(new)
    return result

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
