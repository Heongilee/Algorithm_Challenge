# 백준 6549번
# https://www.acmicpc.net/problem/6549
import sys
import math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
######################################################################################
# segment tree + divide and conquer   Solution.
#################################################################################
def buildSegmentTree(node, start, end):
    if start == end: #leaf 노드라면
        tree[node] = start
    else:
        mid = (start + end) // 2
        buildSegmentTree(node * 2, start, mid)
        buildSegmentTree(node * 2 + 1, mid + 1, end)

        # 더 작은 값의 인덱스를 정복함.
        tree[node] = tree[node * 2] if height[tree[node * 2]] < height[tree[node * 2 + 1]] else tree[node * 2 + 1]

# 트리로 구성된 탐색 구역을 start, end로 나타내고
# 문제에서 주어진 인풋에 대한 범위를 lt와 rt로 표현할 때
def query(node, start, end, lt, rt):
    if lt > end or rt < start:  # 주어진 [start, end] 범위를 완전히 벗어난다면
        return -1
    if lt <= start and end <= rt: # 주어진 [start, end] 범위가 전체를 포함한다면
        return tree[node] # 해당 범위의 최소 index를 리턴함.
    
    mid = (start + end) // 2
    m1 = query(node * 2, start, mid, lt, rt)
    m2 = query(node * 2 + 1, mid + 1, end, lt, rt)

    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return m1 if height[m1] <= height[m2] else m2

def solution(start, end):
    minIdx = query(1, 0, n - 1, start, end)
    area = (end - start + 1) * height[minIdx]

    # minIdx의 양옆을 분할과 정복 수행.
    if start <= minIdx - 1:
        tmp = solution(start, minIdx - 1)
        area = max(area, tmp)   # 넓이가 더 큰 값으로 갱신.
    if minIdx + 1 <= end:
        tmp = solution(minIdx + 1, end)
        area = max(area, tmp)
    
    return area

if __name__ == '__main__':
    result = []
    while True:
        # TIP : 인풋을 한줄에 몇개 받을지 모를때 *가 쓰인다.
        n, *height = list(map(int, input().split()))

        if n == 0:
            break
        
        # tree 인덱스 1부터 시작하기 위해 끝에 +1을 더해줌
        tree = [0] * (pow(2, math.ceil(math.log(len(height), 2)) + 1) - 1 + 1)
        buildSegmentTree(1, 0, n - 1)
        result.append(solution(0, n - 1))

        del tree    # 해당 테스트케이스에서 쓰인 segment tree 초기화
    
    for e in result:
        print(e)