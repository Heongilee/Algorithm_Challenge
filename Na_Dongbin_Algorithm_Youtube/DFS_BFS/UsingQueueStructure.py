import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

from collections import deque

if __name__ == "__main__":
    dq = deque()

    dq.append(5)
    dq.append(2)
    dq.append(7)
    dq.append(3)

    print(dq)

    for _ in range(len(dq)):
        t = dq.popleft()
        print(t, dq)