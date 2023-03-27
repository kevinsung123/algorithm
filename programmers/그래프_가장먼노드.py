from collections import deque


def solution(n, edge):
    answer = 0
    #adj그래프 만듬
    adj=[ []for  i in range(n+1)]
    check=[ 0 for i in range(n+1)]
    print(adj)
    for e in edge:
        src,dest=e
        print(src,dest)
        adj[src].append(dest)
        adj[dest].append(src)
    print(adj)
    q=deque()
    q.append(1)
    check[1]=1
    level=0
    while True:
        #print("level : ",level,"==================")

        for _ in range(len(q)):
            cur =q.popleft()

            #print("cur:",cur)
            for i in adj[cur]:
                if check[i]==0:
                    #print("next :", i)
                    q.append(i)
                    check[i]=1
        level+=1
        if len(q)==0:
            break
        else:
            answer = len(q)
    #print(answer)
    return answer


if __name__=='__main__':
    n=6
    edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    solution(n,edge)

