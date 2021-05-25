import sys
from collections import defaultdict
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호
실제로 가장 많은 케이크 조각을 받는 방청객의 번호

가장 많은 조각을 받도록 예상되는 방청객이 여러 명인 경우에는 번호가 작은 사람을 출력한다.
'''

def update(maxIdx, maxValue, idx, comp):
    if comp > maxValue:
        maxValue = comp
        maxIdx = idx
    return

if __name__ == '__main__':
    L = int(input())
    N = int(input())
    cake = [-1] + [0] * (L + 1)
    Counter = defaultdict(int)
    # 예상 방청객 인덱스
    # 실제 방청객 인덱스
    # 예상 방청객 케익 길이
    # 실제 방청객 케익 길이
    res = [0, 0, 0, 0]
    
    for i in range(1, N + 1):
        lt, rt = map(int, input().split())

        for j in range(lt, rt + 1):
            if cake[j] != 0:
                continue
            cake[j] = i
            Counter[i] += 1
        if Counter[i] > res[3]:
            res[3] = Counter[i]
            res[1] = i
    print("\n".join(map(str, res[:2])))
    