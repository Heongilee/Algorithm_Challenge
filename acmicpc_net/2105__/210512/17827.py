import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
#######################################################################
# BOJ 17827
##################################################################
if __name__ == '__main__':
    n, m, v = map(int, input().split())
    v -= 1
    C = list(map(int, input().split()))

    for _ in range(m):
        i = int(input())
        if i >= n: i = ((i - v) % (n - v)) + v
        print(C[i])

#######################################################################
# Test code
##################################################################
'''
if __name__ == '__main__':
    # 2 ≤ N ≤ 200,000,  노드의 개수
    # 1 ≤ M ≤ 200,000,  질문의 횟수
    # 2 ≤ V ≤ N,        N번 노드가 가리키는 노드의 번호
    n, m, v = map(int, input().split())
    v -= 1
    C = list(map(int, input().split()))   # 1 ≤ Ci ≤ 1,000,000

    # 인덱스를 몇번까지 돌릴지에 대한 변수 K
    # 출력 형식 : 계산된_인덱스(실제_인덱스)
    K = 50
    for idx in range(K + 1):
        if idx >= n:
            tmp = ((idx - v) % (n - v)) + v
            print(str(tmp) + "(" + str(idx) + ")", end=' ')
            print(end=' ')
            continue
        print(str(idx) + "(" + str(idx) + ")", end=' ')
    print()
'''