import sys
sys.stdin = open("./AlgorithmAssets/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# ∴ 퀵 정렬 시간복잡도
#   └ 최악 : O(N ** 2) -> 피봇이 계속해서 범위의 최댓값이나 최솟값으로 편향될 경우...
#   └ 최선 : O(NlogN)
#
# TIP : 퀵-소트에서 피봇을 정하는 기준은 첫번째 원소로 할 수도, 마지막 원소로 할 수도, 
# 랜덤값으로 할 수도 있을 수 있고 지금까지도 꾸준히 피봇을 정하는 기준에 대해서 연구되고 있다.
def swap(p, q):
    arr[p], arr[q] = arr[q], arr[p]
    
def Qsort(lt, rt):
    if lt >= rt: return
    
    pivot = arr[rt] # 피봇을 범위의 맨 마지막 원소로 정함 
    pos = lt
    for i in range(lt, rt):
        if arr[i] < pivot:
            swap(pos, i)
            pos += 1
    swap(pos, rt)
    
    Qsort(lt, pos - 1)
    Qsort(pos + 1, rt)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    Qsort(0, n - 1)
    print("\n".join(map(str, arr)))
    