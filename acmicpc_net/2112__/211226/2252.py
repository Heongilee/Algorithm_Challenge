import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    inDeg = [0] * (n + 1)
    queue = deque()
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        inDeg[b] += 1
    
    for i in range(1, n + 1):
        if inDeg[i] == 0:
            queue.append(i)
    
    while queue:
        t = queue.popleft()
        print(t, end=' ')
        
        for node in graph[t]:
            inDeg[node] -= 1
            
            if inDeg[node] == 0:
                queue.append(node)