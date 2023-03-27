import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    global ans, Map, chk, alpha, dx, dy
    ans = 1
    queue = set()
    queue.add((y, x, Map[y][x]))

    while queue:
        y, x, vis = queue.pop()
        #print(y, x, vis)
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny >= 0 and nx >= 0 and ny < R and nx < C and not Map[ny][nx] in vis:
                queue.add((ny, nx, vis + Map[ny][nx]))
                if ans < len(vis) + 1:
                    ans = len(vis) + 1


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split())
    Map = [list(sys.stdin.readline().strip()) for _ in range(R)]
    alpha = [0 for _ in range(26)]
    chk = [['' for _ in range(C)] for _ in range(R)]
    bfs(0, 0)
    print(ans)
