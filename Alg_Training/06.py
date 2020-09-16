import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(L):
    global cnt
    if(L == M):
        cnt += 1
        for r in res:
            print(r, end=' ')
        print()
        return
    else:
        for n in range(1, N + 1):
            res[L] = n
            DFS(L + 1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    res = [0] * M
    DFS(0)
    print(cnt)