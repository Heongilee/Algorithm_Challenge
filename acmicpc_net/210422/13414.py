import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

##########################################################################
# 98% WA (대체 왜...???)
#####################################################################
def getKey(v):
    return v % 10000

def insertHashTable(V, idx):
    K = getKey(V)

    for i in range(len(hashTable[K])):
        if hashTable[K][i][0] == V:
            tmp = hashTable[K][i][1]    # 인덱스 저장
            hashTable[K][i][1] = idx
            return tmp

    hashTable[K].append([V, idx])
    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    students = list(int(input()) for _ in range(k))
    hashTable = dict(zip(list(map(lambda X : getKey(X), set(students))), list([] for _ in range(len(set(students))))))
    
    for i in range(k):
        t = insertHashTable(students[i], i)
        if t != -1: students[t] = 0

    cnt = 0
    for i in range(len(students)):
        if students[i] != 0:
            print("{:08d}".format(students[i]))
            cnt += 1
            if cnt >= n:
                break
############################################################################
# my answer (Python3 TLE, Pypy3 1% TLE)
#######################################################################
'''
if __name__ == '__main__':
    # 과목의 수강 가능 인원 K (1 ~ 100,000), 
    # 학생들이 버튼을 클릭한 순서를 기록한 대기목록의 길이 L(1 ~ 500,000)
    k, l = map(int, input().split())
    students = deque(list(int(input()) for _ in range(l)))

    for _ in range(l):
        if students[0] in list(students)[1:]:
            students.popleft()
        else:   # students[0] not in students[1:]
            students.append(students.popleft())
    
    print('\n'.join(map(lambda X: str(X).zfill(8), list(students)[:k])))
'''