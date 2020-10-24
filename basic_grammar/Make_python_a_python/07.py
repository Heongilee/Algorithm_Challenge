def solution(mylist):
    answer = list(map(int, mylist))
    return answer

if __name__ == "__main__":
    res = solution(['1', '100', '33'])
    print(res)