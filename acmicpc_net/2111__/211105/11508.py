import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 유제품 2+1 행사
# 3개 제품을 구매 시, 3개 중 하나는 거저줌.
if __name__ == '__main__':
    n = int(input())
    arr = list(int(input()) for _ in range(n))

    answer = 0
    arr.sort(reverse=True)
    for i in range(n):
        if i % 3 == 2:
            continue
        answer += arr[i]
    print(answer)