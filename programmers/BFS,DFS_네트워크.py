from collections import deque


def solution(n, computers):
    answer = 0
    chk = [False]*n
    # n개의 컴퓨터에 대해 bfs
    for i in range(n):
        if not chk[i]:
            q = deque()
            q.append(i)
            chk[i] = True
            while q:
                cur = q.popleft()
                # 현재 노드와 연결된 모든 노드를 방문
                for n, val in enumerate(computers[cur]):
                    #print(n,val)
                    if cur == n:
                        continue
                    # cur노드와 연결되어있고 아직 방문하지 않았다면
                    if val == 1 and not chk[n]:
                        q.append(n)
                        chk[n] = True
            answer += 1
    return answer


if __name__ == '__main__':
    n=3
    #computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))

