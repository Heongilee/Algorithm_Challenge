import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
from bisect import bisect_left as bl

if __name__ == "__main__":
    arr = [1, 2, 4, 4, 8, 16, 32, 67, 128, 256, 521, 1024]
    x = 8

    print(bl(arr, x))
