def odd(x):
    return True if (x % 2 !=0) else False

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

i = 0
j = N // 2
sum = 0
for k in range(N):
    size = (N // 2) if(odd(k)) else (N // 2 + 1)
    
    l = i
    m = j
    for _ in range(size):
        sum += a[l][m]
        l += 1
        m -= 1
    if(odd(k)):
        j += 1
    else:
        i += 1
print(sum)