import sys, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAXIMUM = int(10e8) + 7
def buildTree(start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = buildTree(start, mid, node * 2) * buildTree(mid + 1, end, node * 2 + 1) % MAXIMUM
    return tree[node]

# 구간합의 경우 top-down 방식으로 전체 문제에서 작은 문제로 값을 수정해 나갔다면,
# 구간곱의 경우 bottom-up 방식으로 작은 문제에서 전체 문제로 값을 수정해 나간다는 점이 차이점이다.
def update(start, end, node, idx, value):
    if idx < start or end < idx:
        return
    # tree[node] += value
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)    
    tree[node] = tree[node * 2] * tree[node * 2 + 1] % MAXIMUM

def interval_mul(start, end, node, lt, rt):
    # out of range
    if rt < start or end < lt:
        return 1
    # included segment
    if lt <= start and end <= rt:
        return tree[node]
    
    mid = (start + end) // 2
    return interval_mul(start, mid, node * 2, lt, rt) * interval_mul(mid + 1, end, node * 2 + 1, lt, rt) % MAXIMUM
        

if __name__ == '__main__':
    # 데이터 개수(n), 변경이 일어나는 횟수(m), 구간합을 구하는 횟수(k)
    n, m, k = map(int, input().split())
    
    arr = [-1] + list(int(input()) for _ in range(n))
    tree = [0] * (2 ** (math.ceil(math.log2(len(arr))) + 1))
    
    buildTree(1, n, 1)
    for _ in range(m + k):
        a, b, c = map(int, input().split())
        
        if a == 1:  # b번째 수를 c로 바꿈
            update(1, n, 1, b, c)
            arr[b] = c
        else:       # b부터 c까지 곱을 구함
            answer = interval_mul(1, n, 1, b, c)
            print(answer)