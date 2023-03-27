import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    global target, H, W, Map, dist


    dist[target[0][0]][target[0][1]] = 0
    q = deque()
    for i in range(4):
        q.append((target[0][0], target[0][1], i, 0))

    while len(q) != 0:
        cur = q.popleft()
        cy = cur[0]
        cx = cur[1]
        dir = cur[2]
        cnt = cur[3]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            ncnt = cnt
            if ny >= 0 and ny < H and nx >= 0 and nx < W and Map[ny][nx] != '*':
                if i != dir:
                    ncnt = cnt + 1
                if dist[ny][nx] >= ncnt:
                    dist[ny][nx] = ncnt
                    q.append((ny, nx, i, ncnt))


if __name__ == '__main__':
    W, H = map(int, sys.stdin.readline().split())
    Map = []
    dist = [[sys.maxsize] * W for _ in range(H)]
    target = []

    for _ in range(H):
        tmp = list(sys.stdin.readline().strip())
        Map.append(tmp)

for y in range(H):
    for x in range(W):
        if Map[y][x] == 'C':
            target.append((y, x))
bfs()
print(dist[target[1][0]][target[1][1]])
