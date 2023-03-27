from itertools import permutations

tmp = [[ j for j in range(6)] for i in range(6)]
# for i in permutations(tmp, 6):
#     print(i)
#     print(type(i))
copy=tmp
for i in tmp:
    print(i,end="\n")
tmp[0][0]=7
print("================")
for i in range(6):
     tmp[0][i]=i+5
for i in tmp:
    print(i,end="\n")

tmp=[ row[:] for row in copy]
for i in tmp:
    print(i,end="\n")

