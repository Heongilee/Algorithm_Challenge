def solution(mylist):
    # return list(map(lambda L : len(L), mylist))
    return list(map(len, mylist))
    
if __name__ == '__main__':
    res = solution([[1, 2], [3, 4], [5]])
    print(res)