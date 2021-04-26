import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 키보드 배열에서 문자c가 위치한 인덱스를 리턴함
def findPos(c):
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == c:
                return i, j
    return -1, -1

if __name__ == '__main__':
    sl, sr = input().rstrip().split()
    keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], 
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], 
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    arr = list(input().rstrip())
    
    # 초기 위치 잡기 .
    lx, ly = findPos(sl)
    rx, ry = findPos(sr)

    res = 0
    for c in arr:
        x, y = findPos(c)
        
        flag = None
        if 0 <= x <= 1:
            # 왼손
            if 0 <= y <= 4: flag = 'L'
            # 오른손
            else: flag = 'R'
        else:
            # 왼손
            if 0 <= y <= 3: flag = 'L'
            # 오른손
            else: flag = 'R'
        
        res += (abs(lx - x) + abs(ly - y) if flag == 'L' else abs(rx - x) + abs(ry - y)) + 1
        if flag == 'L': lx, ly = x, y
        else: rx, ry = x, y

    print(res)
        
    '''
    print("lx, ly : ", lx, ly)
    print("rx, ry : ", rx, ry)
    '''