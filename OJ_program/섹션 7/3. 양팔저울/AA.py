def DFS(L, Le, Ri):
    if(Ri - Le > 0 and Ri - Le <= weight(S)):
        chk[Ri - Le] = 0
    if(L == K):
        return
    else:
        DFS(L + 1, Le + S[L], Ri)
        DFS(L + 1, Le, Ri + S[L])
        DFS(L + 1, Le, Ri)

if __name__ == '__main__':
    K = int(input())
    S = list(map(int, input().split()))
#    체크리스트
#    만들 수 없으면 1, 있으면 0
    chk = [1] * (weight(S) + 1)
    chk[0] = -1
    
    DFS(0, 0, 0)
    print(chk.count(1))