import sys, math
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

'''
# MLE
# 재귀 호출
def solution(k, exp, inv):
    if k == 0:
        print(1 if inv % 2 != 0 else 0)
        sys.exit(0)
    else:
        e = int(math.log2(k))
        solution(k - int(math.pow(2, e)), e, inv + 1)

if __name__ == '__main__':
    k = int(input())
    if k != 1: 
        solution(k - 1, int(math.log2(k)), 0)
    print(0)
'''

'''
# MLE
# 무식하게 구하기
if __name__ == '__main__':
    k = int(input())
    kk = int(math.pow(2, math.ceil(math.log2(k))))
    myList = [0]
    rt = 1
    while rt <= kk:
        for lt in range(rt):
            myList.append(0 if(myList[lt] == 1) else 1)
            if len(myList) == k:
                print(myList[-1])
                sys.exit(0)
        rt *= 2
'''