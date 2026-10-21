import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    # result=[]
    # for i in range(len(heap)): #should not be-> for i in heap:
    #     new=heapq.heappop(heap)
    #     result.append(new)
    # return result
 
    return [heapq.heappop(heap) for i in range(len(heap))]

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
