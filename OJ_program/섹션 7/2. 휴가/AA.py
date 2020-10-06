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
