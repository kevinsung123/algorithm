import sys
from collections import deque


def run(n):
    L = [i for i in range(1, n + 1)]
    card = deque(L)
    while len(card) > 1:
        card.popleft()
        card.rotate(-1)
    return card[0]


def main():
    n = int(sys.stdin.readline())
    res = run(n)
    print(res)


if __name__ == "__main__":
    main()
