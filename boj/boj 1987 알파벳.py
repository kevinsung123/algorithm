import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(y, x, length):
    global ans, Map, chk, alpha, dx, dy
    ans = max(ans, length)

    # 방문 체크 및 현재까지 알파벳 경로 체크
    chk[y][x] = 1
    alpha[ord(Map[y][x]) - ord('A')] = 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and nx >= 0 and ny < R and nx < C and alpha[ord(Map[ny][nx]) - ord('A')] != 1 and chk[ny][nx] != 1:
            dfs(ny, nx, length + 1)
    chk[y][x] = 0
    alpha[ord(Map[y][x]) - ord('A')] = 0


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split())
    Map = [list(sys.stdin.readline().strip()) for _ in range(R)]
    alpha = [0 for _ in range(26)]
    chk = [[0 for _ in range(C)] for _ in range(R)]
    ans = 1
    dfs(0, 0, 1)
    print(ans)
    # 공백 포함
    # board = [list(sys.stdin.readline().split()) for _ in range(R)]
    # 공백 미포함
    # board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    # 공백 미포함
    # board = [list(input()) for _ in range(R)]
