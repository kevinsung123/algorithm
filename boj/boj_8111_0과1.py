import sys
from collections import deque
# N의 나머지는 0-N-1
# visited 배열에 나머지들의 방문여부 체크
# 이미 들어있으면 넘어가고 안들어있으면 추가
# 나머지가 0이면 이값은 n의배수이면서 조건을 만족 최소의 수
#
def bfs(n):
    visited = [-1 for _ in range(n )]
    parent = [0 for _ in range(n )]
    pc = [0 for _ in range(n )]
    q = deque()
    q.append(1)
    visited[1] = 0
    parent[1] = -1
    while len(q) > 0:
        cur = q.popleft()
        # 0또는 1을 붙여가면서 체크
        for k in range(2):
            next = (cur * 10 + k) % n
            # 방문하지 않았다면
            if visited[next] == -1:
                print(next)
                parent[next] = cur
                # 문자열 저장
                pc[next] = k
                # 방문체크
                visited[next] = visited[cur]+1
                q.append(next)
    print("vistied : ",visited)
    print("parent : ",parent)
    print("pc : ",pc)
    if visited[0] == -1:
        print("BRAK")
    else:
        cur = 0
        ans = ''
        cur_list=[]
        while parent[cur] != -1:
            cur_list.append(cur)
            ans += str(pc[cur])
            cur = parent[cur]
        ans += '1'
        print("cur_list :")
        for i in cur_list:
            print(i,end=",")
        print()
        print("parent_list :")
        for i in cur_list:
            print(pc[i],end=",")
        print()
        print(''.join(reversed(ans)))


if __name__ == '__main__':

    T = int(input())
    test_case = []
    for _ in range(T):
        n = int(input())
        if n == 1:
            print(n)
        else:
            bfs(n)
