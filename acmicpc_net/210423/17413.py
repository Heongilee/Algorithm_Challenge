import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    S = input().rstrip()

    alpha = 0
    lt, rt = 0, 0
    i = 0
    if '<' in S:
        alpha = 1
    while i < len(S):
        if S[i] == '<' or S[i] == '>':
            rt = i

        if (S[lt] != '<' and S[lt] != '>') and S[rt] == '<':
            T = S[lt:rt].split(" ")
            for i in range(len(T)):
                print(T[i][::-1], end='')
                if i != len(T) - 1:
                    print(" ", end='')
            lt = rt
            i = rt + 1
            continue
        elif S[lt] == '<' and S[rt] == '>':
            print(S[lt:rt + 1], end='')
            lt = rt
            i = rt + 1
            continue
        elif S[lt] == '>' and S[rt] == '<':
            if S[lt + 1:rt] == '':
                lt = rt
                i = rt + 1
                continue
            else:
                T = S[lt + 1:rt].split(" ")
                for i in range(len(T)):
                    print(T[i][::-1], end='')
                    if i != len(T) - 1:
                        print(" ", end='')
                lt = rt
                i = rt + 1
                continue
        i += 1
    if i == len(S):
        T = S[lt + alpha:].split(" ")
        for i in range(len(T)):
            print(T[i][::-1], end='')
            if i != len(T) - 1:
                print(" ", end='')
        print()