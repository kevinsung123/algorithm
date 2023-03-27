import sys


def P(Map, N, M):
    for y in range(N):
        for x in range(M):
            print(Map[y][x], end=" ")
        print()


def R(Map, N, M):
    max_len = 0
    for y in range(N):
        # 숫자와 등장횟수
        cnt = [0] * 101

        # 숫자와 등장횟수 넣을 리스트
        tmp = []
        for x in range(M):
            num = Map[y][x]
            if num != 0:
                cnt[num] += 1
                Map[y][x] = 0

        # 각 행(열)마다 cnt한것을 이차원 리스트에 넣음
        # k = 수
        # v = 횟수
        for k, v in enumerate(cnt):
            # 등장횟수가 0인것들은 제외
            if v != 0:
                print
                # 숫자 먼저 넣고 등장횟수를 넣음
                tmp.append([v, k])
        tmp.sort()
        # 최대 행/열 갱신
        max_len = max(max_len, len(tmp) * 2)
        # 원래 맵에 넣음
        # 0 횟수 1 수
        for k, v in enumerate(tmp):
            # k는 index v는 이차원리스트의 [0]=숫자,[1]=등장횟수
            Map[y][k * 2 + 1] = v[0]
            Map[y][k * 2] = v[1]


    return max_len


if __name__ == "__main__":
    r, c, k = map(int, sys.stdin.readline().split())
    time, ans = 0, -1
    Map = [[0] * 100 for _ in range(100)]
    for y in range(3):
        Map[y][0], Map[y][1], Map[y][2] = map(int, sys.stdin.readline().split())
    N, M = 3, 3

    while time <= 100:
        if Map[r - 1][c - 1] == k:
            ans = time
            break
        if N >= M:
            # R연산을 하므로 최대 열 길이 갱신
            M = R(Map, N, M)
           # P(Map,N,M)
        else:
            Map = list(map(list, zip(*Map)))
            N = R(Map, M, N)
            Map = list(map(list, zip(*Map)))
            #P(Map,N,M)
        time += 1
print(ans)
