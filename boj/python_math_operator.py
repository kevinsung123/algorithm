def L(n):
    tmp1 = n % 1000 * 10
    tmp2 = int(n / 1000)
    print(tmp1 + tmp2)
    return tmp1 + tmp2


def R(n):
    tmp1 = int(n / 10)
    tmp2 = n % 10 * 1000
    return tmp1 + tmp2


for n in [1234, 990, 9090]:
    print("n:", n)
    print("L :",L(n))
    print("R : ",R(n))
