import sys
def tsp(cur, visit):
    global dp, dist, N
    # 모든 곳을 방문 base case
    if visit == (1 << N) - 1:
        return dist[cur][0] if dist[cur][0] > 0 else int(1e9)
    # 이미 방문한곳
    if dp[cur][visit]>0:
        return dp[cur][visit]
    ret = int(1e9)
    for i in range(1,N):
        # i번 마을을 방문했거나 현재 cur 에서 i번으로 갈 수 없는 경우제외
        if visit & (1 << i) or dist[cur][i] == 0:
            continue
        ret = min(ret, tsp(i, visit | (1 << i)) + dist[cur][i])
    dp[cur][visit] = ret
    return ret

if __name__ == '__main__':
    N = int(input())
    # edge 간선 정보
    dist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # vertex 정점 리스트
    dp = [[0] * (1 << N) for _ in range(N)]
    print(tsp(0, 1))
    print(dp)




