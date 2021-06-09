import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    # 1 < L < P < V
    for i, line in enumerate(sys.stdin):
        L, P, V = map(int, line.rstrip().split())
        if not L and not P and not V: break
        div, mod = divmod(V, P)
        print("Case " + str(i + 1) + ":", L * div + (L if mod > L else mod))