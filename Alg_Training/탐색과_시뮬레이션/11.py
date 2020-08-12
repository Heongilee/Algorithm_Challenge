import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = 7
S = 5
a = [list(map(int, input().split())) for _ in range(N)]


def isCircularSentence(b):
    # 회문 검사
    for k in range(S // 2):
        if(b[k] != b[-1-k]):
            break
        else:
            continue
    else:
        return True
    return False


def func1(i, j):
    b = []
    for h in range(j, j + S):
        if(h >= N):
            break
        else:
            b.append(a[i][h])
    else:
        if(isCircularSentence(b)):
            return True
        else:
            return False


def func2(i, j):
    b = []
    for v in range(i, i + S):
        if(v >= N):
            break
        else:
            b.append(a[v][j])
    else:
        if(isCircularSentence(b)):
            return True
        else:
            return False


# Main
cnt = 0
# 회문검사 수평
for i in range(N):
    for j in range(N - S + 1):
        if(func1(i, j)):
            cnt += 1

# 회문검사 수직
for j in range(N):
    for i in range(N - S + 1):
        if(func2(i, j)):
            cnt += 1

print(cnt)
'''
#####################################################################
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        # Slice 기능.
        # 다만, 수평 슬라이싱은 가능한데, 수직으로는 안되기 때문에, 밑에 반복문에선 일일히 리스트에 넣어야 한다.
        tmp = a[j][i:i + 5]
        # 역순 만들어내기
        if(tmp == tmp[::-1]):
            cnt += 1
        for k in range(2):
            if(a[i + k][j] != a[i + 5 - k - 1][j]):
                break
        else:
            cnt += 1
print(cnt)
