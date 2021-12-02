import sys
from collections import defaultdict
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    for line in sys.stdin:
        esc = False
        t = line.rstrip()
        if t == '*': break
        
        for d in range(len(t) - 1): # (N - 2)-쌍 까지 존재.
            dic = defaultdict(int)
            for i in range(len(t) - d - 1):
                my_str = t[i] + t[i + d + 1]
                
                if dic[my_str]:
                    esc = True
                    print(f"{t} is NOT surprising.")
                    break
                dic[my_str] += 1
            if esc: break
        if esc: continue
        print(f"{t} is surprising.")