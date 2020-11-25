import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N, M = map(int, input().split())
    Prob = []   # ProblemValue, ProblemTime
    D = [0] * (M + 1)
    
    for _ in range(N):
        pv, pt = map(int, input().split())
        Prob.append((pv, pt))
    
    for pv, pt in Prob:
        for j in range(M, pt - 1, -1):
            D[j] = max(D[j - pt] + pv, D[j])
    print(D[M])