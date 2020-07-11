import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())

j = 1
for i in range(1, N + 1):
    if(N % i == 0 and j == K):
        print(i)
    elif(N % i == 0):
        j += 1
    else:
        continue