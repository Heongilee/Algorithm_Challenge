import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == "__main__":
    N = int(input())
    D = [0] * (N + 1)
    
    # 직관적으로 알 수 있는 부분은
    # 초기화 한다.
    D[1] = 1
    D[2] = 2
    
    for i in range(3, N + 1): # 3 ~ n까지
        D[i] = D[i - 1] + D[i - 2]
    
    print(D[N])