import sys
sys.stdin = open("./input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input().split()))
    result = 0

    for s in range(n):
        D = dict()
        cnt = 0
        p = s
        res = 0
        
        for _ in range(n):
            cnt += board[p]
            D[cnt] = D.get(cnt, 0) + 1
            p += board[p]
        
        for k, v in zip(D.keys(), D.values()):
            if v >= 2:
                res += 1
        
        result = max(result, res)
    print(result)
        
