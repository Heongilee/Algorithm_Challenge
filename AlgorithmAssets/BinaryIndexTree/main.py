'''
# 0이 아닌 마지막 비트 == 내가 저장하고 있는 값들의 개수

n = 16
for i in range(n + 1):
    print(f"{i}의 마지막 비트 : {i & -i}")
    
# 0의 마지막 비트 : 0
# 1의 마지막 비트 : 1
# 2의 마지막 비트 : 2
# 3의 마지막 비트 : 1
# 4의 마지막 비트 : 4
# 5의 마지막 비트 : 1
# 6의 마지막 비트 : 2
# 7의 마지막 비트 : 1
# 8의 마지막 비트 : 8
# 9의 마지막 비트 : 1
# 10의 마지막 비트 : 2
# 11의 마지막 비트 : 1
# 12의 마지막 비트 : 4
# 13의 마지막 비트 : 1
# 14의 마지막 비트 : 2
# 15의 마지막 비트 : 1
# 16의 마지막 비트 : 16
'''

# Implementation
import sys
sys.stdin = open("./AlgorithmAssets/BinaryIndexTree/input.txt", "rt")
input = sys.stdin.readline

# i번째 수까지의 누적합을 계산
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

# i번째 수를 diff 만큼 더하는 함수
def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

if __name__ == '__main__':
    n, m, k = map(int, input().split()) # 데이터 개수(n), 변경 횟수(m), 구간합 연산 횟수(k)

    arr = [0] * (n + 1)
    tree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        arr[i] = int(input())
        update(i, arr[i])

    for line in sys.stdin:
        a, b, c = map(int, line.rstrip().split())
        
        if a == 1:
            update(b, c - arr[b])
            arr[b] = c
        else:   # a == 2
            result = interval_sum(b, c)
            print(result)