# https://www.acmicpc.net/problem/11053
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    D = [0] * (n + 1)
    arr.insert(0, 0)
    D[1] = 1

    for i in range(2, n + 1):
        M = 0
        for j in range(1, i):
            if(arr[j] < arr[i] and D[i] < D[j]): # 오름 차순인지 확인하고, 나 이전의 녀석들 중 가장 긴 길이를 가진 녀석을 선택한다.
                D[i] = D[j]                
        D[i] += 1 # 가장 긴 녀석들에서 현재 요소를 +1 했을 때 최장 길이가 된다.
    print(max(D))