import heapq as hq  # 1. heapq를 import 한다.

a = []

while(True):
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if(len(a) == 0):
            print(-1)
        else:
            print(-hq.heappop(a))   # 꺼낼 땐 다시 부호를 바꿔서 출력하면 가장 큰 값이 출력된다.
    else:
        hq.heappush(a, -N)  # a 힙의 삽입 시 부호를 바꿔서 넣어 최대힙 효과를 낸다.