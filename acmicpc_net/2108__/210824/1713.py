import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
if __name__ == '__main__':
    n = int(input())    # 1 ~ 20 (사진틀 개수)
    m = int(input())    # <= 1000
    arr = list(map(int, input().split()))
    Pic = dict()

    for i in range(len(arr)):
        stuNo = arr[i]
        if Pic.get(stuNo, 0) == 0:
            if len(Pic) < n:
                Pic[stuNo] = (stuNo, i, 1)
            else:
                # 다 차서 자리가 없다면,,,
                # 1. 추천수가 가장 적은 학생을 빼냄.
                candidates = []
                minCnt = INF
                for k, v in Pic.items():
                    if v[2] < minCnt:
                        minCnt = v[2]
                        candidates = []
                        candidates.append(v)
                    else:
                        candidates.append(v)
                # 2. 추천수가 가장 적은 학생이 여러명이라면, 가장 오래있었던 후보를 빼냄.
                if len(candidates) > 1:
                    key, minSeq = 0, INF
                    for cStuNo, cSeq, cCnt in candidates:
                        if cSeq < minSeq:
                            minSeq = cSeq
                            key = cStuNo
                    Pic.pop(key)
                else:
                    Pic.pop(candidates[0][0])
                Pic[stuNo] = (stuNo, i, 1)
        else:
            Pic[stuNo] = (stuNo, Pic[stuNo][1], Pic[stuNo][2] + 1)
    print(" ".join(map(str, sorted(Pic.keys()))))