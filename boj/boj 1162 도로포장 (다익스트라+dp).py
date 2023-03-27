from heapq import *
import sys

if __name__ == '__main__':
    n, m, k = map(int, sys.stdin.readline().split())
    # 인접리스트
    Map = [[] for _ in range(n + 1)]
    for i in range(m):
        src, desc, cost = map(int, sys.stdin.readline().split())
        Map[src].append((desc, cost))
        Map[desc].append((src, cost))

    # dist 배열 동시에 DP 무한대초기화  dist[n][k]
    dist = [[float('INF')] * (k + 1) for _ in range(n + 1)]
    dist[1][k] = 0
    q = []
    heappush(q, (0, 1, k))
    while q:
        d, cur, cnt = heappop(q)  # d=거리 cur=현재 정점 cnt=도로 포장 가능 횟수
        if dist[cur][cnt] <= d:
            for nx, cost in Map[cur]:
                # 도로 포장 가능한 경우
                if cost > 0 and d < dist[nx][cnt]:
                    dist[nx][cnt - 1] = d
                    heappush(q, (d, nx, cnt - 1))
                if cost < dist[nx][cnt]:
                    dist[nx][cnt] = d
                    heappush(q, (d, nx, cnt))
    print(min(dist[n]))
