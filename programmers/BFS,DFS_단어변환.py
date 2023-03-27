import sys
from collections import deque

transistable = lambda a, b:  sum( 1 if x!=y  else 0 for x,y in zip(a,b))==1

def solutions(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    chk = [False] * len(words)
    level=0
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            answer = cnt
            break
        for idx, next in enumerate(words):
            # cflag = 0
            # for m in range(len(cur)):
            #     if cur[m] != next[m]:
            #         cflag +=1
            cflag=0
            for a,b in zip(a,b):
                if a!=b:
                    cflag+=1
            # 변화하려는 문자열이 알파벳 1개만 다를때
            if cflag == 1 and not chk[idx]:
                q.append((next, cnt + 1))
                chk[idx] = True
        level+=1
   # print(answer)
    return answer

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [False] * len(words)
    stack = [begin]

    while stack:
        x = stack.pop()
        if x == target:
            return answer

        for i, w in enumerate(words):
            if not visited[i] and len([1 for a, b in zip(x, w) if a != b]) == 1:
                visited[i] = True
                stack.append(w)

        answer += 1

    return answer


if __name__ == '__main__':
    begin = 'hit'
    target = 'cog'
    words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    solutions(begin, target, words)
