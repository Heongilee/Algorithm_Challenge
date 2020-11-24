import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == "__main__":
    Kilo = []
    Value = []
    N, W = map(int, input().split())
    D = [0] * (W + 1) # idx KG일때 만들 수 있는 최대 가치.
    mm = 2147000000
    mw = 2147000000
    
    for _ in range(N):
        k, v = map(int, input().split())
        Kilo.append(k)
        Value.append(v)
    
    for k, v in zip(Kilo, Value):
        for j in range(k, W + 1):
            D[j] = max(D[j - k] + v, D[j])
    print(D[W])