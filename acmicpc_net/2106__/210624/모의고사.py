def solution(answers):
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    res = [0, 0, 0]
    i = 0
    while i < len(answers):
        realIdx = i % len(answers)
        for r in range(3):
            if students[r][realIdx % len(students[r])] == answers[i]: res[r] += 1
        i += 1
    criteria = max(res)
    result = []
    for i in range(len(res)): 
        if res[i] == criteria: result.append(i + 1)
    return result

if __name__ == '__main__':
    # res = solution([1,2,3,4,5]) # [1]
    # res = solution([1,3,2,4,2]) # [1, 2, 3]
    res = solution([3, 2])
    print(res)