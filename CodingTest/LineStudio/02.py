def solution(line):
    equation = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            x = 10000
            y = 10000

            # x에 대해...
            equation += (line[i][0] - line[j][0]) * x

            # y에 대해...
            equation += (line[i][1] - line[j][1]) * y

            # 상수에 대해...
            equation += (line[i][2] - line[j][2])

if __name__ == '__main__':
    res = solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
    print(res)
    