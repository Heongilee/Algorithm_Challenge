import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
from collections import deque

# BFS 탐색 알고리즘
def BFS(graph, v):
    dq = deque()
    dq.append(v)
    visit[v] = 1

    while(dq):
        t = dq.popleft()
        print(t, end=', ')

        for e in graph[t]:
            if(visit[e] != 1):
                visit[e] = 1
                dq.append(e)
    return 


def solution(graph):
    dummy = [-1]
    graph.insert(0, dummy)
    
    return BFS(graph, 1)

if __name__ == "__main__":
    N = 8
    visit = [0] * (N + 1)
    solution([[2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]])
    print()