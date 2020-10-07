def DFS(L, tot):
    global cnt
    # if(tot + sum(map(lambda idx:P[idx] * N[idx], range(L, k))) < t):
    #     return
    if(tot > t):
        return
    if(L == k):
        if(tot == t):
            cnt += 1
        return
    else:
        for i in range(N[L] + 1):
            DFS(L + 1, tot + (P[L] * i))
    
if __name__ == '__main__':
    t = int(input())
    k = int(input())
    P = list()  # 동전의 종류
    N = list()  # 동전의 개수
    cnt = 0
    for _ in range(k):
        pi, ni = map(int, input().split())
        P.append(pi)
        N.append(ni)
    DFS(0, 0)
    print(cnt)