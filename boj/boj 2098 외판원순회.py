import sys


# dp[cur][visit] : visit은 방문한 도시들이고 현재 cur일떄, 방문하지 않은 도시들을 모두 방문하고 돌아오는 최단거리비용
def tsp(cur, visit):
    if visit == (1 << N) - 1:
        return dist[cur][0] if dist[cur][0] > 0 else int(1e9)
    ret = dp[cur][visit]
    if ret != -1:
        return ret

    ret = int(1e9)
    for i in range(N):
        # i번마을을 이미 방문했거나 cur->i로 갈수 없는 경우
        if visit & (1 << i) or dist[cur][i] == 0:
            continue
        ret = min(ret, tsp(i, visit | (1 << i)) + dist[cur][i])
    dp[cur][visit] = ret
    return ret


if __name__ == '__main__':
    N = int(input())
    dist = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]
    # 싸이클이 존재하므로 출벌점이 어디든지 모두 같으므로 0번마을을 출발점으로 간주
    print(tsp(0,1))