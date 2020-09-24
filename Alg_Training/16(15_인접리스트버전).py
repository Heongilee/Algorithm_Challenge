import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(v):
    global cnt
    if v == N:
        cnt += 1
    else:
        for nv in g[v]:
            if( ch[nv] == 0):
                ch[nv] = 1
                DFS(nv)
                ch[nv] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    ch = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
    cnt = 0
    ch[1] = 1
    DFS(1)
    print(cnt)
    
    for i in range(1, N + 1):
        print("[", i, "] : ", end='')
        for nv in g[i]:
            print(nv, end=' ')
        print()