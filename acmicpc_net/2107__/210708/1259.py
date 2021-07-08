import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.rstrip()
        if line == '0': break

        myList = list(line)
        L = len(myList) // 2 + (0 if len(myList) % 2 == 0 else 1)
        for i in range(L):
            if myList[i] != myList[::-1][i]:
                print("no")
                break
        else:
            print("yes")
