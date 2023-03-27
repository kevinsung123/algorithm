import sys
from itertools import combinations, permutations

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    perm = permutations(arr, N)
    answer = -10000
    answer_list=()
    for case in perm:
        sum = 0
        for i in range(N-1):
            #print(case[i],case[i+1])
            sum += abs(case[i] - case[i + 1])
        if answer < sum:
            answer=sum
            answer_list=case
    print(answer)
    print(answer_list)
