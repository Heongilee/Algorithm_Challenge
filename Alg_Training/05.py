import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

# Bottom-up 방식(1)
'''
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
'''

# Bottom-up 방식(2)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    dy = [0] * (n + 1)
    dy[1] = 1
    res = 0
    
    for i in range(2, n+1):
        max = 0
        for j in range(i - 1, 0, -1):
            if(arr[j] < arr[i] and dy[j] > max):
                max = dy[j]
        dy[i] = max + 1
        if(dy[i] > res):
            res = dy[i]
    print(res)
