import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

N = int(input())

a = []
for _ in range(N):
    l, w = map(int, input().split())
    
    a.append((l, w))

a.sort(reverse = True)

maxW = -2147000000
cnt = 0
for l, w in a:
    if(w > maxW):
        maxW = w
        cnt += 1

print(cnt)