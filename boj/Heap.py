from heapq import *

num = [4, 1, 7, 3, 8, 5]
q = []
# max heap
print("===========maxheap===========")
for n in num:
    heappush(q, (-n, n))  # 우선순위와 값을 값이넣는다
print("n번쨰 값을 구할때")
print(nlargest(2, q))
while q:
    print(heappop(q)[1])

# main heap
print("==========minheap===========")
minq = []
for n in num:
    heappush(minq, n)
print("The 3 largest numbers in list are : ", end="")
print(nlargest(3, minq))
print("The 3 smallest numbers in list are : ", end="")
print(nsmallest(3, minq))

while minq:
    print(heappop(minq))

print("정렬 ", end=" ")
arr = [9, 1, 6, 4, 2, 8, 3, 7, 5]
print(sorted(arr))
print(sorted(arr,reverse=True)[:3])
print("n번쨰 정렬 ", end=" ")
print(sorted(arr)[0:3]) # 0<= <3