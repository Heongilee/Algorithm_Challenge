################# 최소힙 만들기 ########################
# 최소힙이란? : 부모노드의 값이 자식노드의 값보다 항상 작도록 트리를 구성하는 것.
# 파이썬에서 힙(Heap)을 사용하려면?
import sys
import heapq as hq  # 1. heapq를 import 한다.
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

a = []

while(True):
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if(len(a) == 0):
            print(-1)
        else:
            print(hq.heappop(a))    #hq의 heappop이라는 함수가 a에서 root노드 값을 pop하고 그 root 노드 값을 반환
    else:
        hq.heappush(a, N)   #hq의 heappush(리스트, 값)이라는 함수가 a 힙의 N값을 최소힙 구조에 맞춰 push함.