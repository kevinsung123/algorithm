def sol(n, A):
    global MIN,data,mainA
    if n == K:
        for i in range(N):
            MIN = min(MIN, sum(A[i]))
        return
    for i in range(K):
        if not check[i]:
            r, c, s = data[i]
            #newA = [A[i][:] for i in range(N)]
            newA = [row[:] for row in A]
            for j in range(s):
                y, x = r - s - 1 + j, c - s - 1 + j
                #print("y=",y," x=",x)
                #print("=================")
                # 상->우->하->좌
                for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
                    #print("2*s-2*j=",2*s-2*j)
                    for k in range(2 * s - 2 * j):
                        ny, nx = y + dy, x + dx
                       # print("ny=",ny,"nx=",nx)
                        newA[ny][nx] = A[y][x]
                        y, x = ny, nx

            check[i] = 1
            sol(n+1, newA)
            check[i] = 0
if __name__=='__main__':
    N, M, K = map(int, input().split())
    mainA = [list(map(int, input().split())) for i in range(N)]
    data = [list(map(int, input().split())) for i in range(K)]
    check = [0]*K
    MIN = 99999
    sol(0, mainA)
    print(MIN)