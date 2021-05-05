import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(input())):
        words = list(input().rstrip().split(" "))

        while True:
            ani, *sou = input().rstrip().split(" goes ")

            if not sou: break
            sou = ''.join(sou)
            while sou in words: words.remove(sou)
        print(" ".join(words))