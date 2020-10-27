import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")
'''
if __name__ == '__main__':
    N, K = map(int, input().split())
    cnt = 0
    
    while(N != 1):
        if(N < K):
            break
        while(N % K != 0):
            N -= 1
            cnt += 1
        N //= K
        cnt += 1
    print(cnt)
'''
###############################################################################
N, K = map(int, input().split())

result = 0

while True:
    target = (N // K) * K   # N이 K로 나누어 떨어지는 가장 가까운 수를 찾아냄.
    result += (N - target)  # N - target은 1을 뺀 횟수를 나타냄.
    N = target
    
    if(N < K):
        break
    
    result += 1
    N //= K

result += (N - 1)
print(result)