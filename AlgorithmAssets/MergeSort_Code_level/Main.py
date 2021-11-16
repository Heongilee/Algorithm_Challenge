import sys
sys.stdin = open("./AlgorithmAssets/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# Divide 하는 시간 O(logN)
# Conquer 하는 시간 O(N)
#
# ∴ 병합 정렬 시간복잡도
#   └ 최악 : O(NlogN)
#   └ 최선 : O(NlogN)
# 공간복잡도 O(N)
def Dsort(lt, rt):
    # base-case
    if lt >= rt: return
    
    # divide
    mid = (lt + rt) // 2
    Dsort(lt, mid)
    Dsort(mid + 1, rt)
    
    # and conquer
    tmp = []
    p, q = lt, mid + 1
    while p <= mid and q <= rt:
        if arr[p] < arr[q]:
            tmp.append(arr[p])
            p += 1
        else:
            tmp.append(arr[q])
            q += 1
    if p <= mid: 
        tmp += arr[p:mid + 1]
    if q <= rt:  
        tmp += arr[q:rt + 1]
    
    # tmp 빈 리스트를 arr리스트에 반영
    for i in range(len(tmp)): 
        arr[lt + i] = tmp[i]

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    Dsort(0, len(arr) - 1)
    print(arr)