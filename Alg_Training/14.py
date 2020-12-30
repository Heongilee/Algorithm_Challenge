import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")

if __name__ == "__main__":
    MaxLimit = 2147000000
    N = int(input())
    res = []
    D = list([MaxLimit] * N for _ in range(N))
    for i in range(N):
        D[i][i] = 0

    while(True):
        v1, v2 = map(int, input().split())
        if(v1 == -1 and v2 == -1):
            break

        D[v1 - 1][v2 - 1] = 1
        D[v2 - 1][v1 - 1] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    
    for i in range(N):
        res.append(max(D[i]))
    score = min(res)
    cnt = res.count(score)
    print(score, cnt)
    for i in range(N):
        if(res[i] == score):
            print(i + 1, end=' ')