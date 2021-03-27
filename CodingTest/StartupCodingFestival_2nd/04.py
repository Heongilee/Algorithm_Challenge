import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dic = [input().rstrip() for _ in range(n)]
    q = int(input())
    quest = [input().rstrip() for _ in range(q)]

    for i in range(q):
        cnt = 0
        for j in range(n):
            if quest[i] in dic[j]:
                # print(dic[j], end=' / ')
                cnt += 1
        print(cnt)