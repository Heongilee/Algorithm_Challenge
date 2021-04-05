import sys
import copy as cp
sys.stdin = open("./CodingTest/input.txt", "rt")
input = sys.stdin.readline

rank = [-1, 6, 5, 4, 3, 2, 1]   # '인덱스 값'이하로 번호가 일치할 경우
def solution(lottos, win_nums):
    answer = [6, 6] #최고 순위, 최저 순위
    
    # 최고 순위
    Lottos = cp.deepcopy(lottos)
    WinNums = cp.deepcopy(win_nums)
    cnt = 0
    for i in range(6):
        if Lottos[i] in WinNums:
            cnt += 1
        elif Lottos[i] == 0:
            for j in range(6):
                if WinNums[j] not in Lottos:
                    cnt += 1
                    Lottos[i] = WinNums[j]
                    break
    for r in range(6, -1, -1):
        if rank[r] >= cnt:
            answer[0] = r
            break
    
    # 최저 순위
    Lottos = cp.deepcopy(lottos)
    WinNums = cp.deepcopy(win_nums)
    cnt = 0
    for i in range(6):
        if Lottos[i] == 0:
            continue
        elif Lottos[i] in WinNums:
            cnt += 1

    for r in range(6, -1, -1):
        if rank[r] >= cnt:
            answer[1] = r
            break

    return answer

if __name__ == '__main__':
    # res = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
    # res = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
    res = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
    print(res)