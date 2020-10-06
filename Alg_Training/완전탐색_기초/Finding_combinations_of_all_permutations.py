import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
# DFS를 이용한 순열 조합 모두 구하기 예제

def DFS(L):
    global cnt
    if(L == N):
        cnt += 1
        for x in p:
            print(x, end=' ')
        print()
        return
    else:
        for i in range(1, N + 1):
            if(chk[i] == 0):
                chk[i] = 1
                p[L] = i
                DFS(L + 1)
                chk[i] = 0

if __name__ == '__main__':
    N = int(input())
    p = [0] * N
    chk = [0] * (N + 1)
    cnt = 0
    
    DFS(0)
    print(cnt)