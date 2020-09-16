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
def DFS(L, S):
    global cnt
    if(L == M):
        if(len(set(S)) != M):
            return
        for s in S:
            print(s, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, N + 1):
            DFS(L + 1, S + [i])

if __name__ == "__main__":
    N, M = map(int, input().split())
    chk = [0] * (N + 1)
    cnt = 0
    DFS(0, [])
    print(cnt)
'''
##############################################################################
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