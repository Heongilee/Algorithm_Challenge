import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# i 번째 점프
# t를 점프한 거리
#
# 다리를 건넌다.
# 첫 번째 징검다리에서 시작함
# 첫 점프(i == 1)는 아무데나 점프 가능.
# 두번째 점프(i >= 2)부터 D[i - 1] + k(k >= 1) 만큼 뛰어야 함.
# N번째 징검다리를 반드시 밟아야 함.
# N번째 징검다리를 밟는 순간 끝남.
#
# 밟을 수 있는 징검다리의 최대 개수?

# Binary Search
if __name__ == '__main__':
    int(input())
    for line in sys.stdin:
        t = int(line.rstrip())
        
        lt = 0
        rt = int(t ** 0.5) * 2
        res = None
        while lt <= rt:
            mid = (lt + rt) // 2
            
            if (mid * (mid + 1) // 2) > t:
                rt = mid - 1
            else: # (등차수열_합) <= t
                res = mid
                lt = mid + 1
        print(res)

'''
# 50% TLE
if __name__ == '__main__':
    T = int(input())    # 테스트 케이스
    testCase = list(int(input()) for _ in range(T))
    
    for t in range(T):
        n = 0
        inc = 0
        while n <= testCase[t]:
            inc += 1
            n += inc
        print(inc - 1)
'''