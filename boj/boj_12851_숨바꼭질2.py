import sys
from collections import deque


def bfs():
    global N, K
    q = deque()
    chk = [1e9] * 200000
    # 위치와 시간
    q.append((N, 0))
    chk[N] = 0
    ans = 0
    find = False
    ans_time = 0
    while True:
        # 방법의 수를 찾으므로 같은 level큐 모두 조회
        for _ in range(len(q)):
            cur, time = q.popleft()
            # 찾았을때
            if cur == K:
                ans += 1
                ans_time = time
                find = True
            for ncur, ntime in [(cur + 1, time + 1), (cur - 1, time + 1), (cur * 2, time + 1)]:
                # 범위 벗어날떄
                if ncur < 0 or ncur > 100000:
                    continue

                if chk[ncur] >= ntime:
                    chk[ncur] = ntime
                    q.append((ncur, ntime))
        if find == True:
            return (ans, ans_time)


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    if N == K:
        print(0)
        print(1)
    else:
        ans, ans_time = bfs()
        print(ans_time)
        print(ans)
