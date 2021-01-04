import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    command = [(-1, -2), (-1, 2), (1, 2), (1, -2), (-2, -1), (-2, 1), (2, 1), (2, -1)]
    
    N = list(input())
    p = (ord(N[0]) - ord('a'), int(N[1]) - 1)
    count = 0
    
    for c in command:
        xx = p[0] + c[0]
        yy = p[1] + c[1]
        if(0 <= xx < 8 and 0 <= yy < 8):
            count += 1
    print(count)