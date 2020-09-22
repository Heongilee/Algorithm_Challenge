import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
개 어렵네 ㅁㅊ...
'''
'''
def fact(n):
    if(n == 1):
        return 1
    else:
        return n * fact(n - 1)

def comb(n, r): # n Combination r
    if(r == 0 or n == r):
        return 1
    N = fact(n)
    R = fact(r)
    N_R = fact(n - r)
    return int(N / (R * N_R))

def DFS(L): #decision
    if(L == N):
        tmp = 0
        for it in range(N):
            tmp += base[it] * p[it]
        if(tmp == F):
            print(p)
            sys.exit(0)
        else:
            return
    else:
        for i in range(1, N - sum(chk) + 1):
            decision_j = -1
            for j in range(1, len(chk) + 1):
                if(chk[j] == 0):
                    decision_j = j
                    chk[decision_j] = 1
                    p[decision_j - 1] = j
                    break
            DFS(L + 1)
            chk[decision_j] = 0
            

if __name__ == "__main__":
    N, F = map(int, input().split())
    base = [0] * N
    for i in range(N):
        base[i] = comb(N-1, i)
    p = [0] * N
    chk = [0] * (N + 1)
    DFS(0)
'''
##########################################################################
def DFS(L, sum):
    if(L == N and sum == F):
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, N + 1):
            if(ch[i] == 0):
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0
    
if __name__ == '__main__':
    N, F = map(int ,input().split())
    p = [0] * N     # 만든 순열을 저장할 리스트
    b = [1] * N     # N에 의해 생성된 이항계수
    ch = [0] * (N + 1)  # 체크 변수
    
    # 이항계수 초기화
    for i in range(1, N):
        b[i] = b[i - 1] * (N - i) // i   # 조합 공식의 원리를 이용.
    
    DFS(0, 0)