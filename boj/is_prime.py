n=1000
primes=[]
def eratos():
    for a in range(2, n + 1):
        if sieve[a] == True:
            primes.append(a)
            for b in range(2* a, n+1, a):
                sieve[b] = False



sieve = [False,False] + [True]*(n-1)
eratos()

print(primes)
print(len(primes))


def eratos2():
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정
    sieve = [True] * n
    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for a in range(2, m+1):
        if sieve[a] == True:  # a가 소수인경우
            for b in range(a + a, n, a):  # a이 이후 a의 배수들은 False 판정
                sieve[b] = False
    return [i for i in range(2, n) if sieve[i] == True]

ss=eratos2()
print(ss)
print(len(ss))