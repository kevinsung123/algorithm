from collections import deque

a="abcdef"
print("origin : ",a)
## reverse
print("1.slicing : ",a[::-1])

## LOOP
reverse=[]
index=len(a)
while index>0:
    reverse+=a[index-1]
    index=index-1
print(reverse)
print(''.join(reverse))
print("2. loop : ", ''.join(reverse))

## user join
print("3. join : ",''.join(reversed(a)))

## int -> list
m=1234
print(m)
m_list=str(m)
s=[ i  for i in str(m)]

print(s)
s=deque(s)
print(s)
s.rotate(1)
s=list(s)
print(s)
print(''.join(s))