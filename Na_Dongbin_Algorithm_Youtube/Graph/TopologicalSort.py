#########################################################################################################
# Topological Sort 
# 
# 의의.
#   1. 사이클이 없는 방향 그래프(Directed Acyclic Graph)에서 방향성에 거스르지 않도록 순서를 나열하는 방법.
#
# 조건.
#   1. 사이클이 없는 방향 그래프(DAG)
#
# 알고리즘.
#   진입차수가 0인 모든 노드를 큐에 넣는다.
#   큐가 빌 때 까지...
#       큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#       새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
#
# 특징.
#   1.여러 답이 존재할 수 있다.
#   2. 원소를 방문하기 전 큐가 빈다면, 사이클이 존재한다고 판단할 수 있다. 
#
# 성능.
#   O(V + E)
#########################################################################################################
import sys
from collections import deque
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == '__main__':
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    inDegree = [0] * (v + 1)
    dq = deque([])

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b) #정점 a에서 b로 이동
        inDegree[b] += 1
    
    # 진입 차수가 0인 모든 노드를 큐에 삽입.
    for i in range(1, v + 1):
        if(inDegree[i] == 0):
            dq.append(i)

    while(dq):
        t = dq.popleft()
        print(t, end=' ')
        for e in graph[t]:
            inDegree[e] -= 1
            if(inDegree[e] == 0):
                dq.append(e)
    print()