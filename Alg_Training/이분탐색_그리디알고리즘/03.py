import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
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
rt = sum(a)
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
'''
##########################################################################################
N, M = map(int, input().split()) 
music_time = list(map(int, input().split()))

def Count(capacity):
    cnt = 1
    sum = 0
    for elem in music_time:
        if(sum + elem > capacity):
            cnt += 1
            sum = elem
        else:
            sum += elem
    return cnt
        

lt = 1
rt = weight(music_time)
maxV = max(music_time)
res = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    
    # 맥스값 검사를 안 하면 가장 큰 레코드 값은 DVD에 담을 수 없고 버려지게 된다. (반례 수정)
    if(mid >= maxV and Count(mid) <= M):    
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
        
print(res)