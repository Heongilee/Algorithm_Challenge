import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(n):
    global cnt
    if(n == N):
        cnt += 1
        for e in lt:
            print(e, end=' ')
        print()
        return
    else:
        for i in range(1, N + 1):
            if(g[n][i] == 1 and chk[i] == 0):
                chk[i] = 1
                lt.append(n)
                DFS(i)
                lt.pop()
                chk[i] = 0
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    g = [[0] * (N + 1) for _ in range(N + 1)]
    chk = [0] * (N + 1)
    lt = []
    cnt = 0
    
    for _ in range(M):
        a, b = map(int, input().split())
        g[a][b] = 1
    
    chk[1] = 1
    DFS(1)
    print(cnt)