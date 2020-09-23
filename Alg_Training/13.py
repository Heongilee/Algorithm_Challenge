import sys
import itertools as it # 순열이나 조합을 자동으로 구해주는 라이브러리.
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    for x in it.combinations(a, K):
        if(sum(x) % M == 0):
            cnt += 1
    print(cnt)