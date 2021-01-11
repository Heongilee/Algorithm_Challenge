import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    X = 26
    D = [0] * (X + 1)
    D[1] = 0 # X
    D[2] = 1 # X - 1
    D[3] = 1 # X // 3
    D[4] = 2 # X // 3 - 1 혹은 X // 2 - 1
    D[5] = 1 # X // 5

    for i in range(6, X + 1):
        T = [2147000000] * (4)
        if(i % 5 == 0):
            T[0] = D[i // 5]
        if(i % 3 == 0):
            T[1] = D[i // 3]
        if(i % 2 == 0):
            T[2] = D[i // 2]
        T[3] = D[i - 1]
        D[i] = min(T) + 1
    print(D) 
    print(D[X])
