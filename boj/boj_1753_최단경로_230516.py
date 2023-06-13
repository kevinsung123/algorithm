import sys
from collections import deque
import heapq

if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    INF = 10 ** 9
    dist = [INF for _ in range(V + 1)]

    adj = [[] for _ in range(V + 1)]
    check = [False for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        # 정점 V와 U와 V사이의 거리 W
        adj[u].append([v, w])

    # 시작점 거리는 0
    dist[K] = 0
    q = []
    heapq.heappush(q, (0, K))  # 거리, 노드번호
    # 시작점 넣음
    while q:
            cost, node = heapq.heappop(q)  # 현재 거리 및 node
            # 방문했으면 continue
            if check[node] is True:
                continue
            # 해당 정점 방문 표시
            check[node] = True
            # 입력값 받을때 adj[u].append([v,w])
            # 최단거리 갱신
            for nn, nc in adj[node]:
                total = nc + cost
                if dist[nn] > total:
                    dist[nn] = total
                    heapq.heappush(q, (total, nn))

    # 결과
    # 이미 자기자신은 dist[K] =0 초기화
    for i in dist[1:]:
        if i == INF:
            print("INF")
        else:
            print(i)
