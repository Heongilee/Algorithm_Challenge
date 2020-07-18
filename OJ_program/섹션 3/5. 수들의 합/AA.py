N, M = map(int, input().split())
a = list(map(int, input().split()))

L = 0
R = 1
Tot = a[0]
cnt = 0
while(L != R or L != len(a) - 1):
    if(Tot < M):
        if(R >= len(a)):
            break
        Tot += a[R]
        R += 1
    elif(Tot == M):
        cnt += 1
        Tot -= a[L]
        L += 1
    else:   # Tot > M
        Tot -= a[L]
        L += 1
print(cnt)