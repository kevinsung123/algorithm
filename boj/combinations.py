import sys
from itertools import combinations
from itertools import permutations


def isprime(n):
    if n < 2:
        return False;
    if n % 2 == 0:
        return False
    r = round(n ** 0.5)
    for k in range(2, r, 2):
        if n % k == 0:
            return False
    return True


def eratos():
    n = 1000000000
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정
    sieve = [True] * n
    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for a in range(2, m):
        if sieve[a] == True:  # a가 소수인경우
            for b in range(a + a, n, b):  # a이 이후 a의 배수들은 False 판정
                sieve[b] = False
    return [i for i in range(2, n) if sieve[i] == True]


if __name__ == '__main__':
    # string=input()
    # for i in range(1,len(string)+1): # 길이가 1부터 n까지 모든 순열을 구함
    #     perm = permutations(string, i)
    numbers = "011"
    ans = 0
    check_list = []
    str_set = set()
    for i in range(1, len(numbers) + 1):  # 길이가
        for n in permutations(numbers, i):
            str_set.add(int(''.join(n)))
            # check_list.append(''.join(n))
    check_list = list(str_set)
    check_list = sorted(check_list)
    # print(str_set)
    # print(check_list)
    # for i in check_list:
    #     print(i)

    for k in check_list:
        # print(k)
        if isprime(k):
            ans += 1
    print(ans)
