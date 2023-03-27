import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    INF = int(1e9)
    dist = [[0 if i == j else INF for j in range(M+2)] for i in range(M + 2)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        dist[a][b] = 1
        dist[b][a] = 1
    # i->j 정점으로 가는 최단경로를 구함
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    sum = INF
    for i in range(1, N + 1):
        tmp = 0
        for j in range(1, N + 1):
            if i == j:
                continue
            tmp += dist[i][j]
        if tmp < sum:
            ans = i
            sum = tmp
    print(ans)
