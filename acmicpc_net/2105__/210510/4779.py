import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    for line in sys.stdin:
        t = int(line.rstrip())

        arr = ['-'] * (3 ** t)
        L = len(arr)
        prod = L // 3
        while prod > 0:
            for n in range(1, L // prod + 1):
                if n % 2 == 0:  # 짝수는 없앤다.
                    for j in range(prod * n - prod, prod * n): arr[j] = ' '
            prod //= 3
        print("".join(arr))