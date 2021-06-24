def solution(array, commands):
    res = []
    for i, j, k in commands:
        arr = sorted(array[i - 1:j])
        res.append(arr[k - 1])
    return res
        
if __name__ == '__main__':
    res = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) # [5, 6, 3]
    print(res)