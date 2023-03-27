from itertools import combinations, permutations, product
from sys import stdin


# 1번쨰 방법 비트마스킹 이용
def solution(numbers, target):
    answer = 0
    m = len(numbers)
    # bit 연산자 2^m의 경우수
    for bm in range(1 << m):
        sum = 0
        # 한가지 경우의 수가 정해짐
        for j in range(len(numbers)):
            # 1이면 +
            if bm & (1 << j):
                sum += numbers[j]
            # 0이면 -
            else:
                sum -= numbers[j]

        if sum == target:
            answer += 1
    return answer


# 2번쨰 cartesian product에 대해 구함
def solution2(numbers, target):
    answer = 0
    arr = [(x, -x) for x in numbers]
    # 2개의 쌍에대해 cartesian product를 구함
    s = list(map(sum, product(*arr)))
    print(s.count(target))


# 3번쨰 dfs
def dfs(idx, numbers, target, sum_val):
    global answer
    n = len(numbers)
    # 0 ~n-1까지 모두 다 더한 후 다음 idx=n이면 종료조건
    if idx == n and sum_val == target:
        answer += 1
        return
    if idx ==n:
        return
    for i in [1, -1]:
        dfs(idx + 1, numbers, target, sum_val + numbers[idx] * i)


def solution3(numbers,target):
    answer=0
    dfs(0,numbers,target,0)

    return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    solution3(numbers, target)
