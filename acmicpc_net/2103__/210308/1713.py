# 백준 1713번
# https://www.acmicpc.net/problem/1713
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())    
    m = int(input())   
    arr = list(map(int, input().split()))

    Frame = [(0, 0)] * n

    for i in range(len(arr)):
        t = arr[i]
        for f in range(n):
            if Frame[f] == (0, 0):
                Frame[f] = (t, 1)
                break
            if Frame[f][0] == t:
                Frame[f] = (Frame[f][0], Frame[f][1] + 1)
                break
        else:
            minIdx = 0
            for j in range(1, n):
                if Frame[j][1] < Frame[minIdx][1]:
                    minIdx = j
            
            Frame.pop(minIdx)
            Frame.append((t, 1))
    
    Frame.sort()
    for i in range(n):
        print(Frame[i][0], end=' ')
    print()

