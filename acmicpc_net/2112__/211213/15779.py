import sys
from collections import defaultdict
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
###################################################################
# 부분 성공(70점)
##############################################################
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    
    if n < 3:
        print(n)
        sys.exit(0)
    
    mono_dict = defaultdict(list)
    
    # O(N)시간에 단조 증가 혹은 단조 감소가 되는 부분을 완전 탐색.
    no = 0  # 넘버링할 변수
    for i in range(n - 2):
        if A[i] <= A[i + 1] <= A[i + 2] or A[i] >= A[i + 1] >= A[i + 2]:
            no += 1
            mono_dict[i].append(no)
            mono_dict[i + 1].append(no)
            mono_dict[i + 2].append(no)
    
    answer = 2
    for size in range(3, n + 1):
        sack = defaultdict(int) # K, V = 넘버, 개수
        # 슬라이딩 윈도우"
        for i in range(size):
            for num in mono_dict[i]:
                sack[num] += 1
        
        zigzag_count = 0
        for v in sack.values():
            if v >= 3:
                zigzag_count += 1
        if zigzag_count == 0:
            answer = size
            continue
        
        lt, rt = 0, size - 1
        while True:
            rt += 1
            if rt >= n:
                break
            for num in mono_dict[rt]:
                sack[num] += 1
                if sack[num] == 3:
                    zigzag_count += 1
            
            for num in mono_dict[lt]:
                sack[num] -= 1
                if sack[num] == 2:
                    zigzag_count -= 1
            lt += 1
            
            # do sth
            if zigzag_count:
                continue
            
            # max값 갱신
            answer = size
            break
        
    print(answer)