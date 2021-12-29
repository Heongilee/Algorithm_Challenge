def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def interval_sum(start, end, node, lt, rt):
    # out of range
    if rt < start or end < lt:
        return 0
    # included segment
    if lt <= start and end <= rt:
        return tree[node]
    
    mid = (start + end) // 2
    return interval_sum(start, mid, node * 2, lt, rt) + interval_sum(mid + 1, end, node * 2 + 1, lt, rt)

def update(start, end, node, idx, diff):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start == end: 
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, diff)
    update(mid + 1, end, node * 2 + 1, idx, diff)

INF = int(10e9)
if __name__ == '__main__':
    arr = [5, 8, 7, 3, 2, 5, 1, 8, 9, 8, 7, 3]
    query = [(1, 1, 3), (1, 3, 6), (1, 2, 10), (2, 7, 3), (1, 2, 10)]
    
    # build tree
    # import math
    # tree = [0] * (2 ** (math.ceil(math.log2(len(arr))) + 1))
    tree = [0] * (4 * len(arr)) # 4를 곱하면 모든 범위를 커버할 수 있음 (갯수에 대해 2의 제곱형태의 길이를 가지기 때문)
    init(0, len(arr) - 1, 1)
    
    for command, a, b in query:
        if command == 1:    # 구간 합 구하기 (interval_sum)
            answer = interval_sum(0, len(arr) - 1, 1, a, b)
            print(f"구간 [{a}:{b}]의 합 == {answer}")
        else:               # 특정 값 업데이트
            update(0, len(arr) - 1, 1, a, b - arr[a])
            arr[a] = b