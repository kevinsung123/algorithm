import sys

if __name__ == '__main__':
    N = int(input())
    INF = 10 ** 9
    dist = [[INF] * N for _ in range(N)]
    adj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if adj[i][j] != 0:# i->j : 0이 아니면 갈수있음 0이면 INF 못감
                dist[i][j] = adj[i][j]

   # print(dist)

    # floyd적용 => 실제 i->j로가는 최단거리 저장
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # INF= 못감 그이외에 갈수있음
    for i in range(N):
        for j in range(N):
            if dist[i][j] == INF:
                print(0, end=" ")
            else:
                print(1, end=' ')
        print()
