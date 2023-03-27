import sys
from collections import deque


def bfs():
    global N, K, left, right, chk
    ans = 0
    # 처음시작위치를 넣음 왼쪽줄 맨위칸
    q = deque()
    q.append((0, 0))  # 방향과 위치 (y,x) y=0 왼쪽 y=1 오른쪽
    # 시간
    for time in range(0, N):
        print("time=",time)
        while q:
            y, x = q.popleft()
            print("cur=",y," ",x)
            for ny, nx in (y, x - 1), (y, x + 1), ((y + 1) % 2, x + K):
                #print("next=", ny, " ", nx)
                # 종료조건 clean
                if nx >= N:
                    ans = 1
                    return ans
                # 오른쪽 시간 + 안전한칸 + 아직 방문안한 칸
                if nx > time and arr[ny][nx] == '1' and chk[ny][nx] == 0:
                    chk[ny][nx] = 1
                    q.append((ny, nx))
    return ans


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(2)]
    chk = [[0] * N for _ in range(2)]
    ans = bfs()
    print(ans)
