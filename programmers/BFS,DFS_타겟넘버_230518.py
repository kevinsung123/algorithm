from itertools import combinations, permutations, product
from sys import stdin


# 1번쨰 방법 비트마스킹 이용
def solution(numbers, target):
    answer = 0
    m = len(numbers)
    # bit 연산자 2^m의 경우수
    # ex) 1<<4 --> 10000(2) --> 16(10)
    # range 1 <= bm <=15
    for bm in range(1 << m):
        sum = 0
        # 한가지 경우의 수가 정해짐
        for j in range(len(numbers)):
            # 1이면 + 
            # 0이면 - 취급
            # 0000 ~ 1111
            if bm & (1 << j):
                sum += numbers[j]
            # 0이면 -
            else:
                sum -= numbers[j]
        # 한가지 경우의 수에 총합
        if sum == target:
            answer += 1
    return answer


# 2번쨰 cartesian product에 대해 구함
def solution2(numbers, target):
    answer = 0
    arr = [(x, -x) for x in numbers]
    # 2개의 쌍에대해 cartesian product를 구함
    s = list(map(sum, product(*arr)))
    answer = s.count(target)

    return answer


# 3번쨰 dfs
def dfs(idx, numbers, target, sum_val):
    ret = 0
    n = len(numbers)

    # 마지막 depth 도착 및 값 확인
    if idx==n and target == sum_val:
        return 1

    if idx ==n:
        return 0

    for i in [1,-1]:
        ret+=dfs(idx+1,numbers,target,sum_val+numbers[idx]*i)

    return ret




def solution3(numbers,target):
    answer=dfs(0,numbers,target,0)

    return answer


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution3(numbers, target))

