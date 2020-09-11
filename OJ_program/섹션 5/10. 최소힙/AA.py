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
            print(hq.heappop(a))    #hq의 heappop이라는 함수가 a에서 root노드 값을 pop하고 그 root 노드 값을 반환
    else:
        hq.heappush(a, N)