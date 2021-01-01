import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")
from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = list([0] * (N + 1) for _ in range(N + 1))
    degree = [0] * (N + 1)
    dq = deque([])

    # 그래프화 시키고 진입차수 계산.
    for i in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        degree[b] += 1
    for i in range(1, N + 1):
        if(degree[i] == 0): # 선행해야 할 작업이 없다면...?
            dq.append(i)
    
    while(dq):
        t = dq.popleft()
        print(t, end=' ')
        for i in range(1, N + 1):   # graph 순회...
            if(graph[t][i] == 1):
                degree[i] -= 1
                if(degree[i] == 0):
                    dq.append(i)
    print()