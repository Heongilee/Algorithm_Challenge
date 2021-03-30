import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
import itertools as it
from collections import deque
INF = int(10e9)
'''
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
###########################################################################
# 설계 미스...
######################################################################
# src에서 DFS 탐색을 시작하는데 des 리스트 중 한 개의 원소라도 만난다면 True, 탐색도중 chk배열을 만나면 False
def isItPossible(src, des, chk):
    global flag
    if src in des:
        flag = 1
        return
    if src in chk:
        flag = -1
        return

    for e in city[src][1]:
        isItPossible(e, des, chk)
        if flag == -1 or flag == 1: break
    else:
        return

    return flag

def DFS(L, Wlt, lt, Wrt, rt):
    global flag, res
    if L == n:
        res = min(abs(Wlt - Wrt), res)
        return
    else:
        flag = 0
        if not lt or isItPossible(L + 1, lt, rt) == 1:
            lt.append(L + 1)
            DFS(L + 1, Wlt + city[L + 1][0], lt, Wrt, rt)
            lt.pop()
        flag = 0
        if not rt or isItPossible(L + 1, rt, lt) == 1:
            rt.append(L + 1)
            DFS(L + 1, Wlt, lt, Wrt + city[L + 1][0], rt)
            rt.pop()

if __name__ == '__main__':
    n = int(input())
    city = [[-1]] + [[] for _ in range(n)]
    flag = 0    # 0 이면 탐색 중, 1이면 True를 반환, -1이면 False를 반환
    res = INF
    
    # 도시 인구(city[1]), 연결 요소(city[2]; 리스트 타입)
    for idx, popu in enumerate(list(map(int, input().split()))):
        city[idx + 1].append(popu)
    
    for i in range(1, n + 1):
        m, *l = map(int, input().split())
        city[i].append(l)
    
    DFS(0, 0, [], 0, [])
    print(res)
'''
#######################################################################
# 알고리즘만 참고해서 해결 ver.
##################################################################
def BFS(my_list):
    start = my_list[0]
    visited = [False] * (n + 1)
    dq = deque()
    dq.append(start)
    visited[start] = True

    while dq:
        t = dq.popleft()

        for e in graph[t]:
            if not visited[e] and e in my_list:
                visited[e] = True
                dq.append(e)
    
    return True if all (visited[x] for x in my_list) else False

if __name__ == '__main__':
    n = int(input())
    weight = [-1] + list(map(int, input().split()))
    graph = [[-1]]
    res = INF

    for i in range(1, n + 1):
        m, *l = map(int, input().split())
        graph.append(l)
    
    # 두 그룹으로 나눔
    for i in range(1, n // 2 + 1):
        X = set(range(1, n + 1))
        for x in it.combinations(X, i):
            # X의 여집합
            for y in it.combinations(X.difference(x), n - i):
                # 두 그룹이 연결되어 있으면...
                if BFS(x) and BFS(y):
                    t = abs(sum(map(lambda i: weight[i], x)) - sum(map(lambda j: weight[j], y)))
                    res = min(t, res)
    
    print(res if res != INF else -1)