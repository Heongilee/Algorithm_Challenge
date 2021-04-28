# 백준 2531번
# https://www.acmicpc.net/problem/2531
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
INF = int(10e9)
################################################################################
# 내 풀이 (Index slicing & Set 자료구조 활용) 
###########################################################################
'''
if __name__ == '__main__':
    N, d, k, c = map(int, input().split())
    graph = list(int(input()) for _ in range(N))
    maximum = -INF
    f = False

    for i in range(N, -1, -1):
        T = set(graph[i-k:] + graph[0:i] if (i - k < 0) else graph[i - k:i])
        L = len(T)

        if(L >= maximum):
            maximum = L
            f = False if (c in T) else True
    
    print(maximum + 1 if f else maximum)
'''
################################################################################
#  Other Solution
###########################################################################
if __name__ == '__main__':
    N, d, k, c = map(int, input().split())
    graph = list(int(input()) for _ in range(N))
    for e in graph[:k]:
        graph.append(e)

    dic = {}
    lt = 0
    rt = k - 1
    res = 0
    for i in range(lt, rt + 1):
        dic[graph[i]] = dic.get(graph[i], 0) + 1

    res += len(dic)
    res += 1 if(dic.get(c, 0) == 0) else 0

    while lt < N:
        current_res = 0
        rt += 1
        dic[graph[rt]] = dic.get(graph[rt], 0) + 1
        
        if(dic[graph[lt]] == 1):
            del dic[graph[lt]]
        else:
            dic[graph[lt]] -= 1
        lt += 1

        current_res += len(dic)
        current_res += 1 if(dic.get(c, 0) == 0) else 0
        res = max(current_res, res)
        
    print(res)