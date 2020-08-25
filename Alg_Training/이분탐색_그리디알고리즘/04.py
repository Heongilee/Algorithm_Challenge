import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

N, C = map(int, input().split())
a = []
for _ in range(N):
    a.append(int(input()))
a.sort()

def Count(h):
    cnt = 1
    s = 0   #시작 인덱스
    for i in range(1, N):
        tmp = abs(a[s] - a[i])
        if(tmp >= h):
            cnt += 1
            s = i
    return cnt

lt = 1
rt = max(a)
res = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    
    if(Count(mid) < C):
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1
print(res)