import itertools as it

def isPrime(X):
    if any (X % i == 0 for i in range(2, X)):
        return False
    return True

def solution(nums):
    cnt = 0
    for X in it.combinations(nums, 3):
        if isPrime(sum(X)):
            cnt += 1
    return cnt

if __name__ == '__main__':
    # res = solution([1,2,3,4])   # 1
    res = solution([1,2,7,6,4])   # 4
    print(res)