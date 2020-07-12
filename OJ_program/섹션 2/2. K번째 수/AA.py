# import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

# Test case
T = int(input())

arr = []
# T번의 테스트 케이스 진행
for a in range(T):
    N, s, e, k = map(int, input().split())
    
    # N개의 리스트 원소 삽입
    arr = list(map(int, input().split()))
    
    # list slice기능을 사용하면 sub리스트를 둘 필요가 없어진다.
    arr = arr[s-1:e]
    arr.sort()
    
    print("#", a + 1, " ", arr[k - 1], sep='')