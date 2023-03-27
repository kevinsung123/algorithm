import sys
from collections import deque


def bfs():
    global child, chk, parent
    q = deque()
    q.append(1)
    chk[1] = 1
    while len(q) > 0:
        cur = q.popleft()
        for i in child[cur]:
            if chk[i] == 0:  # 아직 방문하지 않았다면
                q.append(i)
                parent[i] = cur
                chk[i] = 1
    for i in range(2, N + 1):
        print(parent[i])

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    child = [[] for _ in range(N + 1)]
    chk = [0 for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        child[a].append(b)
        child[b].append(a)
    bfs()
