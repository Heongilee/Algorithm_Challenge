import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
from collections import deque
sys.setrecursionlimit(10 ** 6)

def DFS(v):
    if len(graph[S[v]]) == 0:
        for j in bag:
            print(j, end=' ')
        print()
        return
    
    # 백트래킹
    for e in graph[S[v]]:
        if not visited[S[e]]:
            visited[S[e]] = True
            bag.append(e)
            DFS(e)
            bag.pop()

if __name__ == '__main__':
    Skill = list(map(str, input().split()))
    Number = list(range(len(Skill) + 1))
    
    S = dict(zip(Skill, Number))
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    inDeg = [0] * (n + 1)
    dq = deque([])
    visited = [False] * (n + 1)
    bag = []

    # build graph
    for _ in range(n):
        a, b = input().split()
        graph[S[a]].append(b)
        inDeg[S[b]] += 1
    
    # 진입 차수가 0인 노드를 찾음.
    for i in range(n):
        if inDeg[i] == 0:
            bag.append(Skill[i])
            DFS(Skill[i])
            break
    
