def DFS(L, s_sum, t_sum):
    global res
    if(t_sum > M):
        return
    if(L >= N):
        if(s_sum > res):
            res = s_sum
        return
    else:
        DFS(L + 1, s_sum + v[L][0], t_sum + v[L][1])
        DFS(L + 1, s_sum, t_sum)
            

if __name__ == '__main__':
    N, M = map(int, input().split())
    chk = [0] * N
    v = []
    res = -2147000000
    
    for _ in range(N):
        s, t = map(int, input().split())
        v.append((s, t))
    
    DFS(0, 0, 0)
    print(res)