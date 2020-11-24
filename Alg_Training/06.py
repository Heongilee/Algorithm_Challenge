import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    D = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if all (x > a[i] for x in a[1:i]):
            D[i] = 1
        else:
            D[i] = max(list(map(lambda j: D[j] if(a[j] < a[i]) else 0, range(1, i)))) + 1
    print(max(D))