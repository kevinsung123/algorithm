import sys
def solve():
    global S
    S = list(S)
    ans = []
    while len(S) > 0:
        ans.append(''.join(S))
        S.pop(0)
    ans.sort()
    for i in ans:
       print(i)


if __name__ == '__main__':
    S = sys.stdin.readline().strip()
    solve()
