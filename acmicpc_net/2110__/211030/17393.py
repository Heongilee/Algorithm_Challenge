import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 통로는 1 × N 길이의 일자 형태
# 통로의 바닥은 1 × 1 타일
# 각 타일은 잉크지수 Ai 와 점도지수 Bi 

# 각 타일에서 서 있을 때 다이나믹 롤러로 칠할 수 있는 최대의 칸 수
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = [0] * n

    for i in range(n - 1):
        lt = i + 1
        rt = n - 1
        mid = None
        r = i
        while lt <= rt:
            mid = (lt + rt) // 2

            if B[mid] > A[i]:
                rt = mid - 1
            else:
                lt = mid + 1
                r = mid
        result[i] = abs(r - (i + 1) + 1)
    print(" ".join(map(str, result)))

        


'''
# 4% TLE
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = [0] * n
    for i in range(n):
        result[i] = sum(list(map(lambda b: 1 if(b <= A[i]) else 0, B[i + 1:])))
    print(result)[]
'''