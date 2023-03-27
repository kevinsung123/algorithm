# Map = [list( for y in range(3)) for _ in range(3)]
# Map = list(zip(*Map))


Map = []
for y in range(3):
    tmp = []
    for x in range(3):
        tmp.append((y * 3) + (x + 1))
    Map.append(tmp)
print(Map)
print(list(map(list, zip(*Map))))
print(list(zip(*Map))) # 행과 열 뒤집음
N = 3
max_len = 6
for y in range(N):
    for _ in range(max_len - len(Map[y])):
        Map[y].append(0)
print(Map)
print("test====================================")
dic = {}
dic[1] = 1
dic[2] = 1
dic[3] = 5
dic[4] = 8
dic[5] = 2
print("dict: key, vlaue =",dic.items())
print("dict key =",dic.keys())
print("dict value = ",dic.values())
print("dict conver to two dimensions list =")
print(list(map(list, dic.items())))
print("정렬후 ")
sort = sorted(list(map(list, dic.items())), key=lambda x: (x[1], x[0]))
print(sort)
sort = sum(sort, [])
print(sort)

print("이차원 리스트 정렬 ")
m=[]
# m.append([4,8])
# m.append([5,2])
# m.append([1,1])
# m.append([2,1])
# m.append([3,1])
m.append([3,1])
m.append([1,2])
m.append([2,1])
m.append([4,3])

print("정렬전 ")
print(m)
print("정렬 후 ")
print(sorted(m,key=lambda x : (x[1],x[0])))

print("---------------------------------------")
dic = {}
dic['D'] = 1
dic['A'] = 1
dic['C'] = 1
dic['E'] = 5
dic['B'] = 8
dic['K'] = 2
print(dic)
print("sort by value",sorted(dic.items(),key=lambda x: x[1]))
print("sort by value if same, sort by key",sorted(dic.items(),key=lambda x: (x[1],x[0])))
print("sort by valu,key and make list")