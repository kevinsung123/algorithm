from heapq import *

# MinHeap
heap = []
heappush(heap, 7)
heappush(heap, 4)
heappush(heap, 1)
print(heap)
heappop(heap)
print(heap)
print(heappop(heap))

# MaxHeap
h = [1, 3, 7, 4, 10]
heaps = []
for num in h:
    heappush(heaps, (-num, num))
while heaps:
    print(heappop(heaps)[1])
