import sys
def DFS(L, sum, tsum):
    global M
    if(sum + (tot - tsum) < M):
        return
    if(sum > C):
        return
    if(L == len(a)):
        if sum > M:
            M = sum
        return
    else:
        DFS(L + 1, sum + a[L], tsum + a[L])
        DFS(L + 1, sum, tsum + a[L])
    
if __name__ == "__main__":
    C, N = map(int, input().split())
    a = [int(input()) for _ in range(N)]
    M = -1
    tot = weight(a)
    DFS(0, 0, 0)
    print(M)