import sys

for x in range(int(input())):  # 테스트 케이스
    n, m = map(int, sys.stdin.readline().split())  # N,M 입력받음
    printerque = [int(x) for x in sys.stdin.readline().split()]  # 중요도
    count = 0  # 출력될 순서
    while printerque:
        if printerque[0] < max(printerque):  # 더 중요한 문서가 있다면 큐 맨뒤로 재배치
            printerque.append(printerque.pop(0))
            m = (m - 1 + len(printerque)) % len(printerque) #출력된 원소의 위치를 계속 갱신
        elif printerque.index(max(printerque)) == m:  # 제일 중요한 문서의 위치와 문제에서 원하는 위치가 같다면 순서 1증가
            count = count + 1
            break
        else:  # 그렇지않으면 맨앞 원소 출력
            printerque.pop(0)
            count = count + 1
            m = m - 1
    print(count)
