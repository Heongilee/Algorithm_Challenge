import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == "__main__":
    alpha = []
    numeric = []
    n = input()

    cnt = 0
    
    for c in n:
        if c.isalpha():
            alpha.append(c)
        else:
            cnt += int(c)
    alpha.sort()
    print(''.join(alpha) + str(cnt))