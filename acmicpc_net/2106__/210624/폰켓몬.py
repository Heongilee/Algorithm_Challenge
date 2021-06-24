def solution(nums):
    choice = len(nums) // 2
    S = set(nums)

    if len(S) >= choice:
        return choice
    else:
        return len(S)
###############################################################################
# TC 7 ~ 20 TLE 
##########################################################################
'''
import itertools as it
def solution(nums):
    res = 0
    for X in it.combinations(nums, len(nums) // 2):
        arr = [0] * (max(nums) + 1)
        t = 0
        for i in range(len(X)):
            if arr[X[i]] == 0: t += 1
            arr[X[i]] = 1
        if t > res:
            res = t
    return res
'''
        

if __name__ == '__main__':
    res = solution([3,1,2,3])   # 2
    # res = solution([3,3,3,2,2,4])   # 3
    # res = solution([3,3,3,2,2,2])   # 2
    print(res)
    