import sys, heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    S = input().rstrip()
    pq = list(map(lambda i:S[i:], range(len(S))))
    hq.heapify(pq)
    while pq: print(hq.heappop(pq))