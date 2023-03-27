from collections import deque, defaultdict
from heapq import *


def dfs(cur,len):
    global chk, answer, new_tickets
    if len == N+1 :
        return
    if len>N:
        return
    for idx, there in enumerate(new_tickets):
        if cur == there[0] and chk[idx] == 0:
            chk[idx] = 1
            dfs(there[1],len+1)
            answer.append(there[1])


def solution(tickets):
    global answer, chk, N,new_tickets
    answer = []
    chk = [False] * len(tickets)
    N = len(tickets)
    new_tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    print(new_tickets)
    dfs("ICN",0)
    answer.append("ICN")
    return answer[::-1]


if __name__ == '__main__':
    # tickets=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
    tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
    solution(tickets)
