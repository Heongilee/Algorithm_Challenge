# 백준 2042번
# https://www.acmicpc.net/problem/2042
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
'''
import math
############################################################################
# segment tree를 활용한 문제
#
# 세그먼트 트리에 활용되는 예
#   1) 구간 lt와 rt가 주어졌을 때, A[lt] + ... + A[rt] 구하기 (구간의 합)
#   2) i번째 수를 V로 바꾸기. A[i] = V
#
# 구간 합을 구하는데 있어
# node가 담당하고 있는 구간이 [start, end]이고, 합을 구해야하는 구간이 [left, right]라고 했을 때,
#    1. [left, right]와 [start, end]가 겹치지 않는 경우
#    2. [left, right]가 [start, end]를 완전히 포함하는 경우
#    3. [start, end]가 [left, right]를 완전히 포함하는 경우
#    4. [left, right]와 [start, end]가 겹쳐져 있는 경우 (1, 2, 3을 제외한 나머지 경우)
#
# index번째 수를 val로 변경하려면...
#    1. [start, end]에 index가 포함되는 경우
#    2. [start, end]에 index가 포함되지 않는 경우
#######################################################################

# build segment tree
def init(node, start, end):
    # node가 leaf노드인 경우 배열의 원소값을 반환.
    if start == end:
        tree[node] = l[start]
    else:
        # 재귀함수를 가지고 왼쪽 자식 오른쪽 자식 트리를 만들고 합을 저장.
        mid = (start + end) // 2
        LeftChildTree = init(node * 2, start, mid)
        RightChildTree = init(node * 2 + 1, mid + 1, end)
        tree[node] = LeftChildTree + RightChildTree
        
    return tree[node]

# calculate sub summation
# node가 담당하는 구간의 표현 [start, end]
# 합을 구해야 하는 구간 [left, right]
def query(node, start, end, lt, rt):
    # 1. [left, right]와 [start, end]가 겹치지 않는 경우
    if lt > end or rt < start:
        return 0
    # 2. [left, right]가 [start, end]를 완전히 포함하는 경우 (구해야하는 합의 범위가 노드와 그 자식노드의 범위 모두를 포함하기 때문.)
    if lt <= start and end <= rt:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node * 2, start, mid, lt, rt) + query(node * 2 + 1, mid + 1, end, lt, rt)

# idx위치의 값을 diff만큼 update하기 위해 start부터 end범위까지 탐색.
def update(node, start, end, idx, diff):
    # 2. [start, end]에 index가 포함되지 않는 경우
    if idx < start or end < idx:
        return
    
    tree[node] += diff
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)
        

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    tree = [0] * int(pow(2, math.ceil(math.log2(len(l)) + 1)) - 1)

    # build segment tree
    init(1, 0, n - 1)

    for _ in range(m + k):
        a, b, c = map(int, input().split())

        if a == 1:  # b번째 수를 c로 바꾼다.
            b -= 1  # 인덱스 조정
            diff = c - l[b]
            l[b] = c
            update(1, 0, n - 1, b, diff)
        elif a == 2:    # b번째 수 부터 c번째 수 까지의 구간 합을 구한다.
            res = query(1, 0, n - 1, b - 1, c - 1)
            print(res)
'''
#############################################################################################
# BIT(Binary Index Tree) 사용한 풀이
########################################################################################
# i번째 수 까지의 누적합을 구하는 함수
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
    n, m, k = map(int, input().split())

    arr = [0] * (n + 1)
    tree = [0] * (n + 1)

    for i in range(1, n + 1):
        x = int(input())
        arr[i] = x
        update(i, x)
    
    for i in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b, c - arr[b])   # 바뀐 크기(diff)만큼 적용
            arr[b] = c
        else:
            print(intervalSummation(b, c))
