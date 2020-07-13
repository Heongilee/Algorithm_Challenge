# import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

N, K = map(int, input().split())

a = []
sum = []

# 입력
a = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(i != j and j != k and k != i):
                sum.append(a[i] + a[j] + a[k])

sum.sort()

cnt = 0
elem = 0
while(cnt < K):
    elem = sum[len(sum) - 1]
    while(sum[len(sum) - 1] == elem):
        sum.pop()
    cnt += 1

print(elem)