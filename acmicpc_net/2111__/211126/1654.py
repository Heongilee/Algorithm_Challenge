import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    k, n = map(int, input().split())
    arr = [int(input()) for _ in range(k)]
    
    rt = max(arr)
    lt = rt // n if rt // n != 0 else 1
    answer = None
    
    while lt <= rt:
        mid = (lt + rt) // 2
        
        # mid 길이짜리 랜선을 몇 개 만들 수 있을까?
        t = sum([a // mid for a in arr])
        if t < n:
            rt = mid - 1
        else:   # t >= n
            answer = mid
            lt = mid + 1
    print(answer)