import time
import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
##############################################################################
# 경로 압축(Path Compression)한 경우...
##############################################################################
INF = int(1e9)

def findParent(e):
    if(e != parentTable[e]):
        parentTable[e] = findParent(parentTable[e])
    return parentTable[e]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parentTable[b] = a
    else:
        parentTable[a] = b

if __name__ == "__main__":
    v, e = map(int, input().split())
    parentTable = list(range(v + 1))

    start = time.time()
    for _ in range(e):
        a, b = map(int, input().split())
        unionParent(a, b)
    
    end = time.time()
    print(f"time : {round(end - start, 10)}sec")
    # # 각 원소가 속한 집합 찾기
    # print("부모 테이블 : ")
    # for i in range(1, v + 1):
    #     print(i, "번 노드의 부모 집합 : ", findParent(i))
    # print()
    
    # # 집합의 개수 출력하기.
    # countSet = set()
    # for i in range(1, v + 1):
    #     countSet.add(findParent(i))
    # print("집합의 개수 :",len(countSet))

    # # 가장 크기가 큰 집합의 원소개수와 작은 집합의 원소 개수
    # countList = [INF] * (v + 1)
    # for i in range(1, v + 1):
    #     t = findParent(i)
    #     if(countList[t] == INF):
    #         countList[t] = 0
    #     countList[t] += 1
    
    # Maximum = -INF
    # Minimum = INF
    # for i in range(1, v + 1):
    #     if(countList[i] == INF):
    #         continue
    #     if(countList[i] > Maximum):
    #         Maximum = countList[i]
    #     if(countList[i] < Minimum):
    #         Minimum = countList[i]
    # print("Maximum :", Maximum)
    # print("Minimum :", Minimum)