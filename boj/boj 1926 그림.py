import queue
import sys


def bfs(y, x):
    global vis, n, m  # 전역변수
    # queue 인데 자료형이 tuple(y,x)
    q = queue.Queue()
    q.put((y, x))
    vis[y][x] = 1
    area = 1
    # 큐가 비지않아더라면
    while not q.empty():
        cy, cx = q.get()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and vis[ny][nx] == 0 and Map[ny][nx] == 1:
                vis[ny][nx] = 1
                q.put((ny, nx))
                area += 1
    return area


## 전역변수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = 0, 0
## main
if __name__ == '__main__':

    # 크기 및 이차원배열 입력받기
    n, m = map(int, sys.stdin.readline().split())
    Map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    vis = [[0] * m for _ in range(n)]

    area__cnt = 0
    max_area = 0
    for i in range(n):
        for k in range(m):
            # map 1이고 아직 미 방문시
            if Map[i][k] is 1 and vis[i][k] is 0:
                area__cnt += 1  # bfs 돌릴때마다 그림 영역 1개 증가
                tmp = bfs(i, k)  # return 그림 넓이 및 최대값 갱신
                if tmp > max_area:
                    max_area = tmp

    print(area__cnt, max_area)
