from collections import deque


def solution(n, results):
    answer = 0
    INF = 10 ** 9
    # result값이 1명부터 n명이므로 n=n+1
    n = n + 1
    dist = [[0 if i == j else INF for i in range(n)] for j in range(n)]
    # a->b 경기경과를 dist에 초기화
    for i in results:
        win, lose = i
        dist[win][lose] = 1

    # floyd
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist)
    flag = [True for i in range(n)]

    # 경기를 결과를 알 수 있는 선수의 수를 구함
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            if dist[i][j] == INF and dist[j][i] == INF:
                flag[i] = False
    # 선수들을 구함
    for i in range(1,n):
        if flag[i] is True:
            answer+=1
    return answer

if __name__ == '__main__':
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    n = 5
    print(solution(n, results))
    print(solution2(n, results))
