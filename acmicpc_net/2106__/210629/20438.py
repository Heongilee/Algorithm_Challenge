# start at 06.29 13:50
import sys, itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
3 ~ N + 2번까지 번호를 부여받음
지환이가 번호 호명을 Q번 했는데, 출석되지 않은 학생 수?
'''
if __name__ == '__main__':
    # 1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000
    # 학생 수 n
    # 졸고 있는 학생 수 k
    # 출석 코드를 보낼 학생 수 q
    # 주어질 구간의 수 m
    n, k, q, m = map(int, input().split())

    students = [0] * (n + 3)    # 0은 출석 안함, 1은 출석함
    sleep = [0] * (n + 3)    # 1이면 자는학생, 0이면 안 잠
    psum = [0] * (n + 3)        # 누적합
    for s in list(map(int, input().split())): 
        sleep[s] = 1
    for q in list(map(int, input().split())):
        if sleep[q]:
            continue
        inc = q
        while q <= n + 2:
            if sleep[q]:
                q += inc
                continue
            students[q] = 1
            q += inc

    # 3 ≤ S < E ≤ N + 2
    accu = list(it.accumulate(students))
    for _ in range(m):
        s, e = map(int, input().split())
        print(e - s + 1  - (accu[e] - accu[s - 1]))