import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

#######################################################
# 답이 되는 이유
#######################################################
'''
print(0.1 * 0.1 == 0.01)    # False, 왜일까...?

# 파이썬은 부동소수점 오차가 나서 정확하지 않다고 한다.
import decimal
print(float(decimal.Decimal('0.1') * decimal.Decimal('0.1')) == 0.01)   # True

출처 : https://hillier.tistory.com/70
'''
if __name__ == '__main__':
    x, y = map(int, input().split())
    z = (y * 100) // x
    if z < 99:
        answer = 0
        
        lt, rt = 0, int(10e8)
        while lt <= rt:
            mid = (lt + rt) // 2
            t = ((y + mid) * 100) // (x + mid)
            if t <= z:
                lt = mid + 1
            else: # t > percent
                answer = mid
                rt = mid - 1
        print(answer)
    else:
        print(-1)