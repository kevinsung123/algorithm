from collections import deque
import heapq


def solution(n, edge):
    answer = 0
    # 인정 리스트 생성
    INF = 10 ** 9
    dist = [[] for i in range(n + 1)]
    # 방문여부 표시
    check = [False for i in range(n + 1)]

    # 간선정보 갱신
    for e in edge:
        src, dest = e
        dist[src].append(dest)
        dist[dest].append(src)
    # 방문하지않은 정점들 중 거리 짧은 정점 구하기 위한 우선순위 큐
    q = deque()

    # 1번노드
    q.append(1)
    check[1] = 1
    level = 0
    while True:
        print(level)
        for _ in range(len(q)):
            cur = q.popleft()

            for i in dist[cur]:
                if check[i] == False:
                    q.append(i)
                    check[i] = True
        level += 1
        if len(q) == 0:
            break
        else:
            answer = len(q)
    return answer


# 1번노드에서 가장 먼 노드를 구하시오
# 다익스트라를 활용하여 1번 노드로부터 최단거리를 모두 구함
# 그 중 가장 먼 거리의 노드의 정점의 개수를 return
def solution2(n, edge):
    answer = 0
    INF = int(10e9)
    # 거리 배열
    dist = [INF for _ in range(n + 1)]
    # 방문 배열
    check = [False] * (n+1)
    # 인접리스트 구함
    adj = [[] for _ in range(n + 1)]
    # 그래프 초기화
    for a, b in edge:
        adj[a].append((1,b))
        adj[b].append((1,a))
    # 1번노드 자기자신이므로 0
    dist[1] = 0
    q = []  # node와 거리
    heapq.heappush(q, (0, 1)) # 거리와 노드

    while q:
        cost, cur = heapq.heappop(q)

        # 방문 체크
        if check[cur] is True:
            continue
        check[cur] = True
        # 거리 갱신
        for next_cost, next_node in adj[cur]:
            total = cost + next_cost
            if dist[next_node] > total:
                dist[next_node] = total
                heapq.heappush(q, (total, next_node)) # heap에 넣을때 갱시된 거리와 노드를 넣는다
    # 0번 index 미사용 하므로 삭제
    dist = dist[1:]
    answer = dist.count(max(dist))
    return answer


if __name__ == '__main__':
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution2(n, edge))
