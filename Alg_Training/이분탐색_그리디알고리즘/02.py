import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

K, N = map(int, input().split())

a = []
for _ in range(K):
    a.append(int(input()))
    
lt = 1
rt = max(a)
res = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    cnt = weight(map(lambda x: x // mid, a))

    if(cnt < N):
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1

print(res)