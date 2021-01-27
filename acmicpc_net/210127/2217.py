# 백준 2217번
# https://www.acmicpc.net/problem/2217
########################################################################
# N = 6
# 30	20	15	10	5	2
#
# i) 로프 1개를 고려한다고 했을때, 가장 높은 무게를 선택해야하므로
# 고려해야할 로프 = [30] 이 된다.
# 고려해야하는 로프의 최소무게 * 고려하는 로프의 개수 = 로프 1개를 선택했을 때 최대 무게 이므로
# 30 * 1 = 30kg
#
# ii) 로프 2개를 고려한다고 했을 때, 
# 고려해야할 로프 = [30, 20] 이 된다.
# 고려해야하는 로프의 최소무게 * 고려하는 로프의 개수 = 로프 2개를 선택했을 때 최대 무게 이므로
# 20 * 2 = 40kg
#
# iii) 15 * 3 = 45kg
# iv) 10 * 4 = 40kg
# v) 5 * 5 = 25kg
# vi) 2 * 6 = 12kg
#
# ∴ 45kg
########################################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    weight = list(int(input()) for _ in range(n))
    maxWeight = -2147000000

    weight.sort()

    for i in range(n):
        if(weight[i] * (n - i) > maxWeight):
            maxWeight = weight[i] * (n - i)
    print(maxWeight)