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