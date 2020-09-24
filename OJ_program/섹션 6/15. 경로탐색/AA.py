def DFS(n):
    global lt, cnt
    lt.append(n)
    chk[n] = 1
    if(n == N):
        cnt += 1
        return
    else:
        for i in range(1, N + 1):
            if(g[n][i] == 1 and chk[i] == 0):
                DFS(i)
                chk[i] = 0
                lt.pop()
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    g = [[0] * (N + 1) for _ in range(N + 1)]
    chk = [0] * (N + 1)
    lt = []
    cnt = 0
    
    for _ in range(M):
        a, b = map(int, input().split())
        g[a][b] = 1
    
    DFS(1)
    print(cnt)