from collections import defaultdict
import copy

def solution(tickets):
    tickets_dict = defaultdict(list)
    for a, b in tickets:
        tickets_dict[a].append(b)
    visited = ['ICN']
    visited_list = []
    dfs(tickets_dict, 'ICN', visited, visited_list, len(tickets))
    return min(visited_list)

def dfs(tickets_dict, cur, visited, visited_list, n):
    if len(visited)==n+1:
        visited_list.append(visited.copy())
        return
    for c in tickets_dict[cur]:
        temp = copy.deepcopy(tickets_dict)
        temp[cur].remove(c)
        visited.append(c)
        dfs(temp, c, visited, visited_list, n)
        visited.pop()


answer = []
def solution(t):
    global answer
    used = [0 for i in range(len(t))]
    t = sorted(t, key = lambda x: x[1])
    t.reverse()
    dfs(["ICN"], t, used)
    return answer

def dfs(result, t, used):
    global answer
    if len(result) == len(t)+1:
        answer = result.copy()
        return
    for i in range(len(t)):
        if t[i][0] == result[-1] and used[i] == 0:
            result.append(t[i][1])
            used[i] = 1
            dfs(result, t, used)
            result.pop()
            used[i]= 0
