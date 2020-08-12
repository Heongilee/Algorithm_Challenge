import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
# 362
N = int(input())    #홀수로 가정
a = [list(map(int, input().split())) for _ in range(N)] #감의 위치
# 회전 명령 정보
# [*번째 행] [0이면 왼쪽, 1이면 오른쪽] [회전하는 격자의 수, shifting]
M = int(input())    #회전 명령 개수 (1 ~ 10)
b = [list(map(int, input().split())) for _ in range(M)]

# 해당 행에서 n개만큼 왼쪽으로 shifting하는 함수
def L_shift(r, n):
    for _ in range(n):
        tmp = a[r - 1][0]
        for i in range(N - 1):
            a[r - 1][i] = a[r - 1][i + 1]
        a[r - 1][N - 1] = tmp
        

def R_shift(r, n):
    for _ in range(n):
        tmp = a[r - 1][N - 1]
        for i in range(N - 1, 0, -1):
            a[r - 1][i] = a[r - 1][i - 1]
        a[r - 1][0] = tmp
    
for c in b:
    r, d, n = c
    
    if(d == 0):
        L_shift(r, n)
    else:
        R_shift(r, n)
    
    for r in a:
        print(r)

#시계모양 합 구하기
S = 0
E = N - 1
sum = 0
for i in range(N):
    for j in range(S, E + 1):
       sum += a[i][j] 
    if(i < N // 2):
        S += 1
        E -= 1
    else:
        S -= 1
        E += 1
    
print(sum)
'''
######################################################################
N = int(input())    #홀수로 가정
a = [list(map(int, input().split())) for _ in range(N)] #감의 위치
# 회전 명령 정보
# [*번째 행] [0이면 왼쪽, 1이면 오른쪽] [회전하는 격자의 수, shifting]
M = int(input())    #회전 명령 개수 (1 ~ 10)

for i in range(M):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0))
            '''
            # 해설 : 
                a[h - 1].pop(0)
                    파라미터 : 인덱스 번호(비워놓을 경우 맨 끝의 인덱스)
                    리턴 값 : 0번째 인덱스 위치의 원소값
                    0번째 인덱스의 원소를 빼고, 
                    그 위치를 매꾸기 위해 auto shifting이 일어남.
                a[h - 1].append(e)
                    리턴 값 : null
                    e의 값을 리스트 맨 끝에 붙인다.
                    
                ※ 빼 냄과 동시에 append 시킴.
            '''
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())
            '''
            # 해설 : 
                a[h - 1].pop()
                    파라미터 : none
                    리턴 값 : 맨 끝 인덱스의 원소 값
                a[h - 1].insert(idx, e)
                    파라미터 : 
                        idx : 인덱스 번호
                        e : 삽입할 원소
                    리턴 값 : null
                    
                    idx에 해당하는 위치에 e를 삽입시키고,
                    나머지 원소들은 auto shifting이 발생함.
            '''

#시계모양 합 구하기
S = 0
E = N - 1
sum = 0
for i in range(N):
    for j in range(S, E + 1):
       sum += a[i][j] 
    if(i < N // 2):
        S += 1
        E -= 1
    else:
        S -= 1
        E += 1
    
print(sum)