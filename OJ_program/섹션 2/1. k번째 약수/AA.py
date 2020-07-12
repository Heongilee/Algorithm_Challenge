# import os
# import sys

# sys.stdin = open(os.getcwd() + "\\AA\\input.txt", "rt")
N, K = map(int, input().split())

res = 0
cnt = 0
for i in range(1, N + 1):
    if(N % i == 0):
        cnt += 1
    if(cnt == K):
        print(i)
        break
else:
    print(-1)