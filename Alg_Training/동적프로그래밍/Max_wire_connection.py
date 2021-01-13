import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    D = [0] * (n + 1)

    arr.insert(0, 0)
    D[1] = 1
    
    for i in range(2, n + 1):
        D[i] = max(list(map(lambda j: D[j] if(arr[j] < arr[i]) else 0, range(1, i)))) + 1
    print(D[n])