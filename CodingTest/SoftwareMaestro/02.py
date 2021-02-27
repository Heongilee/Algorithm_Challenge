import sys
import heapq as hq
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    p, n, h = map(int, input().split())
    T = dict()
    R = [h] * p
    R.insert(0, 0)
    res = [0] * (p + 1)
    
    for _ in range(n):
        x, y = map(int, input().split())

        if(T.get(x, 0) == 0):
            T[x] = list()
            hq.heappush(T[x], -y)
        else:
            hq.heappush(T[x], -y)
    
    for k in T.keys():
        for _ in range(len(T[k])):
            t = -hq.heappop(T[k])
            
            if(t <= R[k]):
                res[k] += t * 1000
                R[k] -= t
    
    for i in range(1, p + 1):
        print(i, res[i])
