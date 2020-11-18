import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    D = [0] * (N + 1)

    for i in range(1, len(arr)):
        if all(x > arr[i] for x in arr[1:i]):
            D[i] = 1
        else:
            tmp_l = list(map(lambda j: D[j] if(arr[j] < arr[i]) else 0, range(1, i)))
            D[i] = max(tmp_l) + 1
    print(max(D))