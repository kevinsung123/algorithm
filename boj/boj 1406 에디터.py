import sys


def editor():
    s1 = list(sys.stdin.readline().rstrip())
    s2 = []
    n = int(sys.stdin.readline())
    for i in range(n):
        c = sys.stdin.readline()
        if c[0] == 'L':
            if len(s1) != 0:
                s2.append(s1.pop())
        elif c[0] == 'D':
            if len(s2) != 0:
                s1.append(s2.pop())
        elif c[0] == 'P':
            s1.append(c[2])
        elif c[0] == 'B':
            if len(s1) != 0:
                s1.pop()
    s2.reverse()
    print(''.join(s1)+''.join(s2))


if __name__ == '__main__':
    editor()
