import sys
from bisect import bisect_right
from itertools import accumulate
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

##############################################################################################
# other solution (itertools 라이브러리의 accumulate 이용)
#########################################################################################
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(accumulate(list(map(int, input().split()))))

    for _ in range(m):
        print(bisect_right(arr, int(input())))

##############################################################################################
# AC (Python 3)
#########################################################################################
'''
if __name__ == '__main__':
    n, m = map(int, input().split())        # 혁진이가 벌여놓은 일의 개수(n), 
                                            # 시간 동안 몇 개의 일을 처리할 수 있는지 알아볼 개수(m)
                                            # 1 <= n, m <= 200,000
    arr = list(map(int, input().split()))   # 1 <= tn <= 10,000, 각 일의 시간(tn)
    for i in range(1, n): arr[i] = arr[i - 1] + arr[i]

    # Time Complexity : mlog(n)
    for _ in range(m):
        # 혁진이가 일할 수 있는 시간(T)
        # 1 <= T <= 2 * 10  ** 9
        print(bisect_right(arr, int(input())))
'''

##############################################################################################
# 90% TLE (Pypy 3)
#########################################################################################
'''
def bisect_left(arr, t):
    lt, rt = 0, n - 1

    while lt <= rt:
        mid = (lt + rt) // 2

        if t < arr[mid]:
            rt = mid - 1
        else:
            lt = mid + 1
    return lt

if __name__ == '__main__':
    n, m = map(int, input().split())        # 혁진이가 벌여놓은 일의 개수(n), 
                                            # 시간 동안 몇 개의 일을 처리할 수 있는지 알아볼 개수(m)
                                            # 1 <= n, m <= 200,000
    arr = deque(list(map(int, input().split())))   # 1 <= tn <= 10,000, 각 일의 시간(tn)
    for i in range(1, n): arr[i] = arr[i - 1] + arr[i]

    # Time Complexity : mlog(n)
    for _ in range(m):
        # 혁진이가 일할 수 있는 시간(T)
        # 1 <= T <= 2 * 10  ** 9
        print(bisect_left(arr, int(input())))
'''
        

##############################################################################################
# 66% TLE (Pypy3)
#########################################################################################
'''
if __name__ == '__main__':
    n, m = map(int, input().split())        # 혁진이가 벌여놓은 일의 개수(n), 
                                            # 시간 동안 몇 개의 일을 처리할 수 있는지 알아볼 개수(m)
                                            # 1 <= n, m <= 200,000
    arr = deque(list(map(int, input().split())))   # 1 <= tn <= 10,000, 각 일의 시간(tn)
    for _ in range(m):
        T = int(input())    # 혁진이가 일할 수 있는 시간(T)
                            # 1 <= T <= 2 * 10  ** 9
        D = [0] * n
        D[0] = arr[0]
        for i in range(1, n):
            D[i] = D[i - 1] + arr[i]
        
        i = 0
        while i < n and D[i] <= T:
            i += 1
        print(i)
'''

##############################################################################################
# 61% TLE (Pypy 3)
#########################################################################################
'''
if __name__ == '__main__':
    n, m = map(int, input().split())        # 혁진이가 벌여놓은 일의 개수(n), 
                                            # 시간 동안 몇 개의 일을 처리할 수 있는지 알아볼 개수(m)
                                            # 1 <= n, m <= 200,000
    arr = deque(list(map(int, input().split())))   # 1 <= tn <= 10,000, 각 일의 시간(tn)

    tmp = cp.deepcopy(arr)
    for _ in range(m):
        T = int(input())    # 혁진이가 일할 수 있는 시간(T)
                            # 1 <= T <= 2 * 10  ** 9
        cnt, cost = 0, 0
        while arr and cost + arr[0] <= T:
            cost += arr.popleft()
            cnt += 1

        print(cnt)
        arr = cp.deepcopy(tmp)
'''