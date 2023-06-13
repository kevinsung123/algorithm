import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    INF = 10 ** 9

    dist = [[INF] * n for _ in range(n)]
    adj = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # edge정보로 초기화
    for i in range(n):
        for j in range(n):
            if adj[i][j] != 0:
                dist[i][j] = adj[i][j]

    # 플로이드
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 출력
    for i in range(n):
        for j in range(n):
            # 가는 경로 없으면 0
            if dist[i][j] == INF:
                print(0, end=" ")
            # 가는 경로 있으면 1 출력
            else:
                print(1, end=" ")
        print()
