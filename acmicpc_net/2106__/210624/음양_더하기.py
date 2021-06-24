def solution(absolutes, signs):
    res = 0
    for n, s in zip(absolutes, list(map(lambda s: 1 if s else -1, signs))): res += n * s
    return res

if __name__ == '__main__':
    res = solution([4,7,12], [True,False,True]) # 9
    # res = solution([1, 2, 3], [[False,False,True]]) # 0
    print(res)
