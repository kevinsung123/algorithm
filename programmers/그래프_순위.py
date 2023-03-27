from collections import deque


def solution(n, results):
    answer = 0
    INF = int(1e9)
    dist = [[0 if i == j else INF for j in range(n+1)] for i in range(n+1)]
    for i in results:
        win, lose = i
        dist[win][lose] = 1
    # floyd
    for k in range(1,n + 1):
        for i in range(1,n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    flag = [True for i in range(n+1)]
    # print(flag)
    # for i in range(1,n+1):
    #     for j in range(1,n+1):
    #         print(dist[i][j],end="\t")
    #     print()
    # 승패를 알 수 없는 경우
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if dist[i][j] == INF:
                if dist[j][i] == INF:
                    flag[i] = False
                    break
    for i in range(1, n + 1):
        if flag[i] is True:
            answer += 1
    return answer


if __name__ == '__main__':
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    n = 5
    solution(n, results)
