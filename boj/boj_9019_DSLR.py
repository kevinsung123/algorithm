import sys
from collections import deque


def D(n):
    return (n * 2) % 10000
def S(n):
    if n == 0:
        return 9999
    else:
        return n - 1
def L(n):
    tmp1 = n % 1000 * 10
    tmp2 = int(n / 1000)
    # print(tmp1 + tmp2)
    return int(tmp1 + tmp2)
def R(n):
    tmp1 = int(n / 10)
    tmp2 = n % 10 * 1000
    return int(tmp1 + tmp2)


def bfs():
    global A, B
    route = "DSLR"
    # 현재까지 이동경로 저장
    dir = ['0'] * 10000
    # parent 배열 초기화
    parent = [-1] * 10000
    visited = [-1] * 10000
    q = deque()
    visited[A] = 1
    q.append(A)
    while q:
        cur = q.popleft()
        next=cur
        # A->B를 찾았을떄
        if cur == B:
            # B->A로 역추적을 시작
            idx = B
            ans = ""
            while parent[idx] != -1:
                ans += (dir[idx])
                idx = parent[idx]
            print(ans[::-1])
            break
        # D,S,L,R 연산 시작
        for i in range(4):
            if i == 0:
                next = (cur * 2)%10000
            elif i == 1: # cur =0 일떄 체크해야하는 데 next를 체크함..
                next = 9999 if cur == 0 else cur - 1
            elif i == 2:
                next = L(cur)
            elif i == 3:
                next = R(cur)
            # parent  조심 parent 방문 안했다는 조건이 빠졌음
            # A가 다시 나올 수있으므로 방문조건을 잘 체크해야댐
            if visited[next] == -1:
                visited[next] = 1
                parent[next] = cur  # 방문 체크 겸 부모 배열저장
                dir[next] = route[i]
                q.append(next)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        # print(A, B)
        # A->B탐색
        bfs()
