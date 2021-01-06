import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
sys.setrecursionlimit(10**6)

# DFS 탐색 알고리즘
def DFS(graph, v):
    global visit
    visit[v] = 1
    print(v, end=', ')
    if all (x == 1 for x in visit[1:]):
        return
    else:
        for i in range(len(graph[v])):
            if(visit[graph[v][i]] == 0):
                DFS(graph, graph[v][i])

def solution(graph):
    dummy = [-1]
    graph.insert(0, dummy)
    
    return DFS(graph, 1)

if __name__ == "__main__":
    N = 8
    visit = [0] * (N + 1)
    solution([[2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]])
    print()