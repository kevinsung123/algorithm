def doR(arr):
    global R, C
    mx = 0
    for i in range(R):
        cnt = [0] * 101
        new = []
        for j in range(C):
            if arr[i][j] != 0:
                cnt[arr[i][j]] += 1
                arr[i][j] = 0
        for k, x in enumerate(cnt):
            if x != 0:
                new.append([x, k])
        new.sort()
        mx = max(mx, len(new) * 2)
        # 수->회수 순서로 넣음
        for k, x in enumerate(new):
            arr[i][k * 2 + 1], arr[i][k * 2] = x
    C = mx


def doC(arr):
    global R, C
    mx = 0
    for j in range(C):
        cnt = [0] * 101
        new = []
        for i in range(R):
            if arr[i][j] != 0:
                cnt[arr[i][j]] += 1
                arr[i][j] = 0
        for k, x in enumerate(cnt):
            if x != 0:
                new.append([x, k])
        new.sort()
        if mx < len(new) * 2:
            mx = len(new) * 2
        # 수->회수 순서로 넣음
        for k, x in enumerate(new):
            arr[k * 2 + 1][j], arr[k * 2][j] = x
    R = mx


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(3):
        arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())

    R, C = [3, 3]
    cnt = 0
    while arr[r - 1][c - 1] != k and cnt <= 100:
        if R >= C:
            doR(arr)
        else:
            doC(arr)
        cnt += 1
    if cnt <= 100:
        print(cnt)
    else:
        print(-1)
