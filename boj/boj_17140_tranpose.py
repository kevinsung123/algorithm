import sys
from heapq import *


def Print(a, n, m):
    print(n, m)
    for y in range(n):
        for x in range(m):
            print(a[y][x], end=" ")
        print()


def R(Map, N, M):
    max_len = 0
    for y in range(N):
        count_dict = {}  # dict에서 map사용
        for x in range(M):
            num = Map[y][x]
            Map[y][x] = 0
            if num == 0:  # 0이면 무시
                continue;
            if num in count_dict:  # 중복된 key값 들어오면 cnt++
                count_dict[num] += 1
            else:  # key값이 처음이면 1
                count_dict[num] = 1
        # (횟수, 수)를 기준으로 list에 넣고 정렬하기
        pq = []
        for key in sorted(sorted(count_dict.keys()), key=lambda x: count_dict[x]):
            pq.append(key)  # 수 먼저 넣고
            pq.append(count_dict[key])  # 횟수
        max_len = max(max_len, len(pq))
        # 정렬한 배열을 원본 배열에 넣음
        for key, v in enumerate(pq):
            Map[y][key] = v
    return max_len


if __name__ == '__main__':
    # 전역변수
    N, M = 3, 3
    Map = [[0] * 101 for _ in range(101)]
    r, c, k = map(int, sys.stdin.readline().split())
    # 3X3 배열에 입력값 넣음
    for y in range(3):
        Map[y][0], Map[y][1], Map[y][2] = map(int, sys.stdin.readline().split())
    ans = -1
    for time in range(101):
        if Map[r - 1][c - 1] == k:
            ans = time
            break
        if N >= M:
            M = R(Map, N, M)
        else:
            Map = list(map(list, zip(*Map)))
            N = R(Map,M,N)
            Map = list(map(list, zip(*Map)))
    print(ans)