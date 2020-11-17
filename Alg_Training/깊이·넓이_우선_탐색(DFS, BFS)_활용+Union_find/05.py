import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Test Bench
'''
'''
def DFS(L):
    global res
    if(L == N):
        if(sum(max(map(list, P))) - sum(min(map(list, P))) < res):
            res = sum(max(map(list, P))) - sum(min(map(list, P)))
            print(P)
        return
    else:
        for i in range(len(P)):
            P[i].append(coin[L])
            DFS(L + 1)
            P[i].pop()
            

if __name__ == '__main__':
    N = int(input())
    coin = [int(input()) for _ in range(N)]
    P = [[0 for c in range(3)] for r in range(3)]
    for i in range(3):
        P[i].clear()
    res = 2147000000
    
    DFS(0)
    print(res)
'''
#################################################################################
'''
Wrong Answer
'''
'''
def DFS(L):
    global res
    if(L == N):
        if(max(P) - min(P) < res):
            res = max(P) - min(P)
        return
    else:
        for i in range(len(P)):
            P[i] += coin[L]
            DFS(L + 1)
            P[i] -= coin[L]

if __name__ == '__main__':
    N = int(input())
    coin = [int(input()) for _ in range(N)]
    P = [0, 0, 0]
    res = 2147000000
    
    DFS(0)
    print(res)
'''
#################################################################################
def DFS(L):
    global res
    if(L == n):
        cha = max(money) - min(money)
        if(cha < res):
            # 단 세 사람의 총액은 서로 달라야 합니다.
            tmp = set()
            for x in money:
                tmp.add(x)
            if(len(tmp) == 3):
                res = cha
        return
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]

if __name__ == '__main__':
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)