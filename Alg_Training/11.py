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
'''
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
'''
##################################################################
# chk 리스트가 필요 있었을까??
def DFS(L, S, sum):
    global cnt
    if(L == K):
        if(sum % M == 0):
            cnt += 1
        return
    else:
        for i in range(S, N):
            DFS(L + 1, i + 1, sum + a[i])

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    
    DFS(0, 0, 0)
    print(cnt)