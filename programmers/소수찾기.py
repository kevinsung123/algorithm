from itertools import permutations

n = 1000
primes = []
# seive = [False] * 2 + [True] * (n - 2)
sieve = [False] * 2 + [True] * (n -2)
primes = []
test = [False,False]+ [True]*(n-1)  # 0 부터 1000


def eratos():
    for a in range(2, n + 1):
        if sieve[a] == True:
            primes.append(a)
            for b in range(2* a, n+1, a):
                sieve[b] = False



def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(n ** 0.5) + 1  # 주의해야함 ! +1
    for k in range(3, r, 2):
        if n % k == 0:
            return False
    return True


def solution(numbers):
    str_set = set()  # unique 순열수
    answer = 0  # 소수의 개수
    for i in range(1, len(numbers) + 1):  # 길이1부터 N까지 순열을 구함
        for n in permutations(numbers, i):
            str_set.add(int(''.join(n)))  # obejct->string->int
    check_list = list(str_set)

    check_list.sort()
    for k in check_list:
        if isprime(k):
            answer = answer + 1
    return answer


if __name__ == '__main__':
    #eratos()
    # for idx, val in enumerate(sieve):
    #     print(idx, val)
    # print(primes)
    print(len(sieve))
    print(len(test))