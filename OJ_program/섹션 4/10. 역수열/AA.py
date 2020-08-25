N = int(input())
a = list(map(int, input().split()))
res = [0] * len(a)
for n, cnt in enumerate(a):
    n += 1
    pt = 0
    i = 0
    while(i < cnt):
        if(res[pt] == 0):
            i += 1
        pt += 1
    while(res[pt] != 0):
        pt += 1
    res[pt] = n

# 출력
for e in res:
    print(e, end=' ')