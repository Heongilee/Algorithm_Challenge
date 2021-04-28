import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
if __name__ == '__main__':
    n = int(input())    # 2 <= n <= 10만
    arr = list(map(int, input().split()))
    result = [None, None, INF]  # 용액1, 용액2, 0에 가장 가까운 값

    arr.sort()
    for i in range(n):
        lt, rt = 0, n - 1
        while lt <= rt:
            mid = (lt + rt) // 2

            if i != mid:    # 같은 용액 노노
                t = abs(arr[i] + arr[mid])
                if t < result[2]: result = [arr[i], arr[mid], t]

            if arr[i] + arr[mid] < 0:
                lt = mid + 1
            elif arr[i] + arr[mid] > 0:
                rt = mid - 1
            else:
                break   # 더 찾을 필요도 없다

    print(' '.join(map(str, sorted(result[:2]))))