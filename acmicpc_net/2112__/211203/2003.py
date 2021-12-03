import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

#################################################################
# 투 포인터(Two pointer), 슬라이딩 윈도우
############################################################
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    lt, rt = 0, 0
    cnt = 0
    summation = sum(arr[lt:rt + 1])
    while True:
        if summation == m:
            cnt += 1
        
        if summation < m:
            rt += 1
            if rt >= n: break
            summation += arr[rt]
        else:
            summation -= arr[lt]
            lt += 1
            if lt >= n: break
            if lt > rt:
                rt += 1
                summation = sum(arr[lt:rt + 1])
    print(cnt)
        

#################################################################
# 구간합 (Binary Index Tree)
############################################################
'''
def prefixSummation(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

# i번째 수를 diff만큼 업데이트 하는 함수
def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)

# 구간합을 구하는 함수
def intervalSummation(start, end):
    return prefixSummation(end) - prefixSummation(start - 1)

if __name__ == '__main__':
    # N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
    n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    tree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        update(i, arr[i])
    
    lt, rt = 1, 1
    cnt = 0
    while lt < n + 1 and rt < n + 1:
        t = intervalSummation(lt, rt)
        # 합이 m이 되는 경우 카운트
        if t == m:
            cnt += 1

        if t < m:
            rt += 1
        else:   # t >= m
            lt += 1
            if lt > rt:
                rt += 1
    print(cnt)            
'''