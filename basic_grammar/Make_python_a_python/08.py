def solution(mylist):
    answer = list(map(len, mylist))
    return answer

if __name__ == '__main__':
    res = solution([[1, 2], [3, 4], [5]])
    print(res)
    