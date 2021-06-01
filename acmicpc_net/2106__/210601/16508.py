import sys, itertools as it
from collections import defaultdict
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

####################################################################
# AC Other solution (https://subong0508.github.io/problem-solving/2021/01/29/BOJ-16508.html)
###############################################################
if __name__ == '__main__':
    T = input().rstrip()
    N = int(input())
    items = []
    res = None

    for i in range(N):
        price, alphas = input().rstrip().split()
        items.append((int(price), alphas))
    
    for n in range(1, N + 1):
        for item in it.combinations(items, n):
            # print(item)
            dic = defaultdict(int)
            for _, alphas in item:
                for a in alphas: dic[a] += 1
            
            cnt = 0
            for t in T:
                if dic[t] > 0:
                    dic[t] -= 1
                    cnt += 1
            
            if cnt != len(T): continue
            tmp = sum([price for price, _ in item])
            res = min(tmp, res) if res != None else tmp

    print(res if res != None else -1)
    

####################################################################
# 11% WA
###############################################################
'''
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
INF = int(10e9)
def DFS(L):
    global res
    if L == len(T):
        ss = set(S)
        tot = 0
        for e in ss: tot += pays[e]
        
        if tot < res: res = tot
        return

    for idx in dic[T[L]]:
        S.append(idx)
        DFS(L + 1)
        S.pop()
        
if __name__ == '__main__':
    T = input().rstrip()
    N = int(input())
    pays = []
    dic = defaultdict(list)
    res = INF

    for i in range(N):
        price, alphas = input().rstrip().split()

        pays.append(int(price))
        for a in set(alphas):
            dic[a].append((i, alphas.count(a)))

    S = list()
    for t in T: print(dic[t])
    # DFS(0)

    # print(res if res != INF else -1)
'''
    
####################################################################
# 38% WA
###############################################################
'''
INF = int(10e9)
if __name__ == '__main__':
    T = input().rstrip()
    N = int(input())
    items = []

    for _ in range(N):
        money, alphas = input().rstrip().split()

        chk = [0] * len(T)
        for i in range(len(T)):
            if T[i] in alphas: chk[i] = 1
        
        items.append((sum(chk), int(money), alphas))
    
    items.sort(key=lambda X: (-X[0], X[1]))
    print(items)

    items.sort(key=lambda X: (X[1], -X[0]))
    print(items)
'''

'''
INF = int(10e9)
if __name__ == '__main__':
    T = input().rstrip()
    N = int(input())
    items = []

    for _ in range(N):
        money, alphas = input().rstrip().split()

        chk = [0] * len(T)
        for i in range(len(T)):
            if T[i] in alphas: chk[i] = 1
        
        items.append((sum(chk), int(money), alphas))
    
    items.sort(key=lambda X: (-X[0], X[1]))
    
    Tchk = [False] * len(T)
    res1, cnt = 0, 0
    for _, money, alphas in items:
        f = False
        for e in alphas:
            for i in range(len(T)):
                if Tchk[i]: continue
                if e == T[i]:
                    cnt += 1
                    f = True
                    Tchk[i] = True
                    break
        if f: res1 += money
        if cnt >= len(T): break
    if cnt < len(T): res1 = INF

    items.sort(key=lambda X: (X[1], -X[0]))
    Tchk = [False] * len(T)
    res2, cnt = 0, 0
    for _, money, alphas in items:
        f = False
        for e in alphas:
            for i in range(len(T)):
                if Tchk[i]: continue
                if e == T[i]:
                    cnt += 1
                    f = True
                    Tchk[i] = True
                    break
        if f: res2 += money
        if cnt >= len(T): break
    
    if cnt < len(T): res2 = INF

    # print(res1, res2)
    print(-1 if min(res1, res2) == INF else min(res1, res2))
'''