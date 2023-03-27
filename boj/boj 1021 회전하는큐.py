import collections


def main():
    n, m = map(int, input().split())
    # 회전하는 큐 생성
    dq = collections.deque()
    [dq.append(x) for x in range(1, n+1)]

    # 찾는 숫자 위치
    find = [int(x) for x in input().split()]

    ans = 0
    for v in find:
            # 2, 3번 연산 최솟값 찾기
            left = dq.index(v, 0, len(dq))
            right = len(dq) - left
            # 첫번째 원소 뽑는경우
            if dq[0] == v:
                dq.popleft()
            # 해당 원소 찾을떄 까지 왼쪽회전
            else:
                if left < right:
                    dq.rotate(-1*left)
                    ans += left
                    dq.popleft()
                else:
                    dq.rotate(right)
                    ans += right
                    dq.popleft()
    print(ans)


if __name__ == "__main__":
    main()