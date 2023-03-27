import sys
from heapq import *

def solve():
    global N, M, r, c, k,Map,cnt
    for t in range(101):  # 시간 0초부터 100초까지
        if Map[r - 1][c - 1] == k:
            print(t)
            return
        if N >= M:  # R연산
            for y in range(N):
                count_dict = dict()  # dict에서 map사용
                for x in range(M):
                    num = Map[y][x]
                    Map[y][x] = 0
                    if num == 0:  # 0이면 무시
                        continue;
                    if num in count_dict:  # 중복된 key값 들어오면 cnt++
                        count_dict[num] += 1
                    else:  # key값이 처음이면 1
                        count_dict[num] = 1
                # (횟수, 수)를 기준으로 list에 넣고 정렬하기
                pq = []
                # q = []
                # print("정렬전===========")
                # print(count_dict)
                # print("정렬후===========")
                # print(sorted(count_dict.items(), key=lambda x: (x[1], x[0])))
                for key,value in sorted(count_dict.items(), key=lambda x: (x[1],x[0])):
                    pq.append(key)  # 수 먼저 넣고
                    pq.append(value)  # 횟수
                M = max(M, len(pq))
                m = len(pq)
                # 정렬한 배열을 원본 배열에 넣음
                for key, v in enumerate(pq):
                    Map[y][key] = v
                #Print(Map, N, M)


        else:
            #Print(Map, N, M)
            for x in range(M):
                count_dict = {}
                # Map 활용하여 숫자 카운트 세기
                for y in range(N):
                    num = Map[y][x]
                    Map[y][x] = 0
                    if num == 0:
                        continue
                    if num in count_dict:
                        count_dict[num] += 1
                    else:
                        count_dict[num] = 1
                pq = []
                for key in sorted(sorted(count_dict.keys()), key=lambda x: count_dict[x]):
                    pq.append(key)
                    pq.append(count_dict[key])
                    # 최대 행 길이 갱신
                N = max(N, len(pq))
                m = len(pq)
                # 원본배열에 넣기

                for key, v in enumerate(pq):
                    Map[key][x] = v
    # 100초 초과시시
    print(-1)
    return

if __name__ == '__main__':
    Map = [[0] * 101 for _ in range(101)]
    cnt = 0
    N, M = 3, 3
    r, c, k = map(int, sys.stdin.readline().split())
    # 3X3 배열에 입력값 넣음
    for y in range(3):
        Map[y][0], Map[y][1], Map[y][2] = list(map(int, sys.stdin.readline().split()))

    solve()
