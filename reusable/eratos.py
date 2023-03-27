from itertools import permutations


def eratos(n):
    sieve = [False] * 2 + [True] * (n - 2)
    
    # n의 최대약수가 sqrt(n)이므로 i=sqrt(n)까지 검사
    k = int(n ** 0.5)+1
    for i in range(2, k):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(2 * i, n, i): # i 이후의 i배수들은 False 판정
                sieve[j] = False
    # 소수목록 출력
    print([i for i in range(2, n) if sieve[i] == True])


if __name__ == '__main__':
    n = 50
    eratos(n)
