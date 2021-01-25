import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
import heapq as hq
#################################################################################
# Kruskal's Algorithm for solving MinimumSpanningTree problem...
#
# 1. 간선 데이터를 비용 기준 오름차순 정렬.
# 2. 간선을 하나씩 확인하며 사이클이 발생하는지를 확인함.
#   (1). 사이클이 발생하면, MST에 포함시키지 않습니다.
#   (2). 사이클이 발생 않하면, MST에 포함시킵니다.
# 3. 모든 간선에 대해 2번을 반복합니다.
#
# 성능 분석 : O(e * log(e))
#################################################################################
def findParent(e):
    if(e != parent[e]):
        parent[e] = findParent(parent[e])
    return parent[e]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    v, e = map(int, input().split())
    pq = []
    parent = list(range(v + 1))
    weight = 0

    for _ in range(e):
        a, b, w = map(int, input().split())
        hq.heappush(pq, (w, a, b)) # 가중치 오름차순으로 원소를 뽑기위해 우선순위큐에 삽입. 
    
    while pq:
        w, a, b = hq.heappop(pq)

        # 사이클을 만드는 간선인지 확인하고, 아니라면...    
        if(findParent(a) != findParent(b)):
            unionParent(a, b)
            weight += w
    # 출력
    print("Minimum cost :", weight)