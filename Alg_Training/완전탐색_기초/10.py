import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(L, S):
    global cnt
    if(L == M):
        cnt += 1
        for r in res:
            print(r, end=' ')
        print()
        return
    else:
        for i in range(S, N + 1):
            res[L] = i
            DFS(L + 1, i + 1)

if __name__ == '__main__':
    N, M = map(int, input().split())
    cnt = 0
    res = [0] * M
    
    DFS(0, 1)
    print(cnt)