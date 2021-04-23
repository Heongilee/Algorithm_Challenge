import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    k, l = map(int, input().split())
    students = [input().rstrip() for _ in range(l)]
    hashMap = dict()

    # build HashMap
    for i in range(len(students)):
        if hashMap.get(students[i], 0) != 0:
            t = hashMap[students[i]]
            students[t] = None
        hashMap[students[i]] = i
    
    res = deque(sorted(hashMap.items(), key=lambda x:x[1]))
    i = 0
    while res and i < k:
        print(res.popleft()[0])
        i += 1