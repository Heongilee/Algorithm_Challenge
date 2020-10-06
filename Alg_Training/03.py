import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
'''
def DFS(L, Le, Ri):
    if(Ri - Le > 0 and Ri - Le <= sum(S)):
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
    chk = [1] * (sum(S) + 1)
    chk[0] = -1
    
    DFS(0, 0, 0)
    print(chk.count(1))
######################################################################################
# sum이 음수면 그릇을 왼쪽에 놓았을 때라는 뜻.
# sum이 양수면 그릇을 오른쪽에 놓았을 때라는 뜻.
# sum의 절댓값은 측정할 수 있는 물의 무게.
'''
def DFS(L, sum):
    global res
    if(L == n):
        if 0 < sum <= s:
            res.add(sum)
        return
    else:
        DFS(L + 1, sum + G[L])
        DFS(L + 1, sum - G[L])
        DFS(L + 1, sum)
    
if __name__ == '__main__':
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s - len(res))
'''