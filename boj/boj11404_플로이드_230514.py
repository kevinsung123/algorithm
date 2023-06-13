import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    # 간선정보 a->b로 가는 비용 C
    edge = []
    # 거리 배열
    # dist[i][i] =0 그 이외에는 무한대로 초기화 왜나하면 최소거리를 구하기때문
    dist = [[0 if i == j else int(1e9) for i in range(101)] for j in range(101)]
    # 버스 정보 입력받음
    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        # array index 0부터 시작
        a= a -1
        b = b-1
        # 최소거리로 일단 초기화
        dist [a][b] = min (dist[a][b],c)
    # 플로이드 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # dist[i][j] > dist[i][k]+dist[k][j] 의 최솟값으로 갱신
                dist[i][j] = min (dist[i][j],dist[i][k]+dist[k][j])
    # print
    for i in range(n):
        for j in range(n):
            # 만약 i에서 j로 갈수 없는 경우에는 그 자리에 0을 출력한다
            if dist[i][j] >= int(1e9):
                print(0, end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
