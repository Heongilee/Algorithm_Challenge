
N, M = map(int, input().split())

a = list(map(int, input().split()))

# mid 값으로 몇 개를 만들 수 있는지 반환하는 함수
def count(mid):
    s = 0
    cnt = 0
    i = 0
    while(i < len(a)):
        if(s + a[i] <= mid):
            s += a[i]
            i += 1
        else:
            s = 0
            cnt += 1
            continue
    return cnt + 1
    

lt = 1
rt = weight(a)
result = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    
    res = count(mid)
    
    if(res > M):
        lt = mid + 1
    elif(res <= M):
        result = mid
        rt = mid - 1
        
print(result)