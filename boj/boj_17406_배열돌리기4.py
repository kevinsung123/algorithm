import sys
from itertools import permutations
import copy


def rotate(r, c, s):
    global arr, N, M
    while s > 0:
        tmp = arr[r - s][c - s]
        for y in range(r - s + 1, r + s + 1):  # 좌 : x좌표는 고정
            arr[y - 1][c - s] = arr[y][c - s]
        for x in range(c - s + 1, c + s + 1):  # 하 : y좌표는 고정
            arr[r + s][x - 1] = arr[r + s][x]
        for y in range(r + s - 1, r - s - 1, -1):  # 우 x좌표는 고정
            arr[y + 1][c + s] = arr[y][c + s]
        for x in range(c + s - 1, c - s - 1, -1):  # 상 : y좌표는 고정
            arr[r - s][x + 1] = arr[r - s][x]
        arr[r - s][c - s + 1] = tmp
        s -= 1

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    tmp_arr = arr
    r_cnt = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    # print(r_cnt)
    perm = [i for i in range(K)]
    ans = 1e9
    for case in permutations(perm, K):
        # 돌릴 횟수를 정하고 나면 돌려줌 그 순서대로
        arr=[ row[:] for row in tmp_arr]
        for i in case:
            r = r_cnt[i][0] - 1
            c = r_cnt[i][1] - 1
            s = r_cnt[i][2]
            rotate(r, c, s)
        ans = min(ans, min([sum(row) for row in arr]))
    print(ans)
