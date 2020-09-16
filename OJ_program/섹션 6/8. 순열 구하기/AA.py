def DFS(L):
    global cnt
    if L == M:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, N + 1):
            if(chk[i] == 0):
                chk[i] = 1
                res[L] = i
                DFS(L + 1)
                chk[i] = 0  # check 변수를 취소시켜준다. 
            
if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    chk = [0] * (N + 1)
    res = [0] * M
    DFS(0)
    print(cnt)