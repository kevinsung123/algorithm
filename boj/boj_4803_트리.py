import sys
from collections import deque


def bfs(node):
    global chk, child, n, m, ans
    nodeCnt = 1
    edge = 0
    chk[node] = 1
    q = deque()
    q.append(node)
    while len(q) > 0:
        cur = q.popleft()
        edge += len(child[cur])
        for next in child[cur]:
            if chk[next] == 0:
                chk[next] = 1
                nodeCnt += 1
                q.append(next)

    if nodeCnt-1 == int(edge / 2):
        ans += 1
    #print(node-1,int(edge/2))

if __name__ == '__main__':
    cnt = 0
    while True:
        ans = 0
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        #   초기화
        chk = [0 for _ in range(502)]
        child = [[] for _ in range(502)]
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            #print(a, b)
            child[a].append(b)
            child[b].append(a)
        for i in range(1, n + 1):
            #print("{}번노드".format(i))
            if chk[i] == 0:
                bfs(i)

        cnt += 1
        if ans == 0:
            print('Case {0}: No trees.'.format(cnt))
        elif ans == 1:
            print('Case {0}: There is one tree.'.format(cnt))
        else:
            print('Case {0}: A forest of {1} trees.'.format(cnt, ans))
