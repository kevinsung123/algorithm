# Q) 1000이하의 소수를 모두 구하시오

def eratos(n):
    global sieve
    m = int(n ** 0.5) + 1
    for a in range(2, m):
        if sieve[a] == True:
            for b in range(a + a, n, a):  # step=a
                sieve[b] = False

    return [i for i in range(2, n) if sieve[i] == True]


if __name__ == '__main__':
    n = 1000
    sieve = [False, False] + [True] * n
    prime = eratos(n)
    print(prime)
    print(len(prime))
