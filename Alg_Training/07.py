import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    N = int(input())
    block = []
    D = [0] * (N + 1)
    for _ in range(N):
        s, h, w = map(int, input().split())
        block.append([s, h, w])
    block.sort(key=lambda x: x[0], reverse=True)
    block.insert(0, [-1])
    for i in range(1, N + 1):
        if all(S[0] < block[i][0] for S in block[1:i]):
            D[i]=block[i][1]
        else:
            tmp_l=list(map(lambda j: D[j] if(block[j][2] > block[i][2]) else 0, range(1, i)))
            D[i]=max(tmp_l) + block[i][1]
    print(max(D))