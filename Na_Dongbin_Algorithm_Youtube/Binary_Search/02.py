import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
from bisect import bisect_left, bisect_right

def countByRange(arr, lvalue, rvalue):
    rIndex = bisect_right(arr, rvalue)
    lIndex = bisect_left(arr, lvalue)

    return rIndex - lIndex

if __name__ == '__main__':
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    count = countByRange(arr, x, x)
    if(count == 0):
        print(-1)
    else:
        print(count)