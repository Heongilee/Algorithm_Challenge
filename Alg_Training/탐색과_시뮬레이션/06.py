import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = int(input())
a = []
for i in range(N):
    e = list(map(int, input().split()))
    a.append(e)

Max = -2147000000

#행 기준 검사
for i in range(N):
    sum = 0
    for j in range(N):
        sum += a[i][j]
    if(sum > Max):
        Max = sum

# 열 기준 검사
for i in range(N):
    sum = 0
    for j in range(N):
        sum += a[j][i]
    if(sum > Max):
        Max = sum

# 우측에서 내려가는 대각선 검사
for k in range(N):
    i = 0
    j = k
    sum = 0
    while(j >= 0):
        sum += a[i][j]
        i += 1
        j -= 1
    if(sum > Max):
        Max = sum

# 좌측에서 내려가는 대각선 검사
for k in range(N - 1, -1, -1):
    i = 0
    j = k
    sum = 0
    while(j < N):
        sum += a[i][j]
        i += 1
        j += 1
    if(sum > Max):
        Max = sum

print(Max)
'''
#################################################################################
N = int(input())

# TIP : 2차원 배열 읽는 방법!
a = [list(map(int, input().split())) for _ in range(N)]

largest = -2147000000

# 각 행과 열의 합 중의 최대를 구함.
for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if(sum1 > largest):
        largest = sum1
    if(sum2 > largest):
        largest = sum2

sum1 = sum2 = 0
for i in range(N):
    sum1 += a[i][i]
    sum2 += a[i][N-i-1]
if(sum1 > largest):
    largest = sum1
if(sum2 > largest):
    largest = sum2
    
print(largest)