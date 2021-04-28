# 백준 1976번
# https://www.acmicpc.net/problem/1976
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
#################################################################
# 틀렸습니다.  -> 왜?>????
############################################################
'''
sys.setrecursionlimit(10** 6)

def DFS(v):
    global desIdx
    global visited
    if v == path[desIdx]:
        visited = [False] * (n + 1)
        desIdx += 1
        if(desIdx == n):
            print("YES")
            sys.exit(0)
    for e in graph[v]:
        if not visited[e]:
            visited[e] = True
            DFS(e)

if __name__ == '__main__':
    n = int(input())    # 도시의 수
    m = int(input())    # 여행 계획에 속한 도시의 수
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    res = False

    for i in range(1, n + 1):
        t = list(map(int, input().split()))

        for j in range(1, n + 1):
            if(t[j - 1] == 1):
                graph[i].append(j) 
    path = list(map(int, input().split()))
    desIdx = 1

    print(graph)
    DFS(path[0])
    print("NO")
'''
##############################################################################################
def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

def findParent(v):
    if v != parent[v]:
        parent[v] = findParent(parent[v])
    return parent[v]

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    parent = list(range(n + 1))

    for i in range(n):
        t = list(map(int, input().split()))
        for j in range(n):
            if(t[j] == 1):
                unionParent(i + 1, j + 1)
    
    path = list(map(int, input().split()))
    res = set(list(findParent(e) for e in path))
    print("YES" if (len(res) == 1) else "NO")
