import sys
from collections import deque


def find(x):
    global parents, chk
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def merge(x, y):
    global parents, chk
    x = find(x)
    y = find(y)

    if x == y or chk[x] == 0 or chk[y] == 0:
        chk[y] = 0
        chk[x] = 0
    # y를 x의 서브트리에 넣는다
    parents[y] = x


if __name__ == '__main__':
    cnt = 0
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        # 초기화
        parents = [i for i in range(n + 2)]  # 부모=자기자신 노드가 1개짜리
        chk = [1 for _ in range(n + 2)]  # 자기자신이 루트인 트리
        ans = 0
        # print(parents)
        # print(chk)
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            merge(a, b)

        for i in range(1, n + 1):
            if chk[find(i)] == 1:
                chk[find(i)] = 0
                ans += 1

        cnt += 1
        if ans == 0:
            print('Case {0}: No trees.'.format(cnt))
        elif ans == 1:
            print('Case {0}: There is one tree.'.format(cnt))
        else:
            print('Case {0}: A forest of {1} trees.'.format(cnt, ans))