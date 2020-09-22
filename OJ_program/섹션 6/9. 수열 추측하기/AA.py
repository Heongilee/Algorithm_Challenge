import sys

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