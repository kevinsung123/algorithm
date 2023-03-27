import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    edge = []
    dist = [[0 if i == j else int(1e9) for j in range(101)] for i in range(101)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        a = a - 1
        b = b - 1
        # edge 정보
        dist[a][b] = min(dist[a][b], c)
    # floyd
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # 이제 dist 배열은 실제로 최단거리르 담고있음
    for i in range(n):
        for j in range(n):
            if dist[i][j]>=int(1e9):
                print(0,end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
