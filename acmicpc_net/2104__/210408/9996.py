import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
########################################################################
# 패턴을 포함하고 있는 문자열을 찾아라 (X)
# 패턴을 완성시켰을때 테스트 케이스(t)의 문자가 되어야 한다.(O)
###################################################################
'''
if __name__ == '__main__':
    n = int(input())
    front, back = map(str, input().rstrip().split("*"))

    for _ in range(n):
        t = input().rstrip()
        i = 0
        for string in [front, back]:
            ok = False
            if string != '':
                while True:
                    while i < len(t) and t[i] != string[0]:
                        i += 1
                    if i >= len(t):
                        break
                    if t[i] == string[0]:
                        if t[i:i + len(string)] == string:
                            i += len(string)
                            ok = True
                            break
                        else:
                            i += 1
                            continue
            else:
                continue

            if ok:
                continue
            else:
                print("NE")
                break
        else:
            print("DA")
'''
#########################################################################
# Solution
####################################################################
n = int(input())
pattern = input().rstrip().split("*")
front = pattern[0]
back = pattern[1]

for _ in range(n):
    string = input().rstrip()
    if string[:len(front)] == front and string[-len(back):] == back and len("".join(pattern)) <= len(string):
        print("DA")
    else:
        print("NE")