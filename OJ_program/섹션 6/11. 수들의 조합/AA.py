def DFS(L, S_idx, sum):
    global cnt
    if(L == K):
        cnt += 1 if (sum % M == 0) else 0
        return
    else:
        for i in range(S_idx, N):
            if(chk[i] == 0):
                chk[i] = 1
                DFS(L + 1, i + 1, sum + a[i])
                chk[i] = 0
            

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    chk = [0] * N
    cnt = 0
    M = int(input())
    
    DFS(0, 0, 0)
    print(cnt)