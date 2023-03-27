import sys
from collections import deque


def bfs():
    global N,K
    q=deque()
    # 현재 위치와 시간의 상태를 가짐
    q.append((N,0))
    # 방문여부 확인
    chk=[1e9]*200000
    chk[N]=0
    while True:
        # level별
        for _ in range(len(q)):
            cur_loc,cur_time=q.popleft()
            if cur_loc==K:
                break
            # 다음 위치
            for next_loc,next_time in [(cur_loc-1,cur_time+1), (cur_loc+1,cur_time+1),(cur_loc*2,cur_time) ]:
                # 다음 위치가 이미방문했으나 최소인 시간이 걸리는 경우
                if next_loc<0 or next_loc >100000:
                    continue
                if chk[next_loc]>=next_time :
                    chk[next_loc]=next_time
                    q.append((next_loc,next_time))
        if chk[K]!=1e9:
            print(chk[K])
            break

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    if N==K:
        print(0)
    else:
        bfs()