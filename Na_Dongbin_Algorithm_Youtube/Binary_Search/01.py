import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

def solution(mid, r):
    res = 0
    for cake in r:
        if(cake <= mid):
            continue
        else:
            res += cake - mid
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    ans = -1
    
    lt = 0
    rt = max(r)

    while(lt <= rt):
        mid = (lt + rt) // 2

        res = solution(mid, r)
        if(res > m):
            ans = mid
            lt = mid + 1
        elif(res < m):
            rt = mid - 1
        else:
            ans = mid
            break
    print(ans)