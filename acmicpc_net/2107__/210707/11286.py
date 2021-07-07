import sys, heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    absHq = []
    int(input())
    for line in sys.stdin:
        t = int(line)
        if t != 0: hq.heappush(absHq, (abs(t), 1 if t > 0 else -1))
        else:
            if not absHq:
                print(0)
                continue
            value, flag = hq.heappop(absHq)
            value *= flag
            print(value)
