import sys


def remove(node):
    global child
    try:
        child[parent[node]].remove(node)
    except ValueError:
        pass


def dfs(node):
    global N, child, M, ans, parent
    if node == M:
        return
    if len(child[node]) == 0:
        ans += 1
        return
    for i in range(N):
        if parent[i] == node:
            dfs(i)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ans = 0
    # 자식노드를 담는 리스트
    child = [[] for _ in range(N)]
    # i번쨰 노드의 부모노드를 입력받음
    parent = list(map(int, sys.stdin.readline().split()))
    # i : 자식노드 parent : 부모노드 자식노드수를 저장
    for i, node in enumerate(parent):
        if node == -1:
            root = i
        else:
            child[node].append(i)
    # 지울노드 입력받으면 지울노드의 부모노드 자식수 감소
    M = int(sys.stdin.readline())

    # 자식 제거
    remove(M)

    dfs(root)
    print(ans)
