import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
'''
'''
def DFS(L, ps):
    global res
    if(L > N + 1):
        return
    if(L == N + 1):
        if(ps > res):
            res = ps
        return
    else:
        DFS(L + v[L][0], ps + v[L][1])
        DFS(L + 1, ps)

if __name__ == '__main__':
    N = int(input())
    v = [(-1, -1)]
    for _ in range(N):
        T, P = map(int, input().split())
        v.append((T, P))
    res = -2147000000
    
    DFS(1, 0)
    print(res)
'''
#####################################################################
def DFS(L, sum):
    global res
    if L == n + 1:
        if sum > res:
            res = sum
        return
    else:
        if L + T[L] <= n + 1:
            DFS(L + T[L], sum + P[L])
        DFS(L + 1, sum)
    
if __name__ == '__main__':
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)