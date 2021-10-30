import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# 보고서의 모든 글자가 A와 B로 바뀜
# 좋은 단어 == 같은 글자끼리 쌍을 지어(A는 A끼리, B는 B끼리) 아치형 선을 그었을 때, 
if __name__ == '__main__':
    answer = 0
    n = int(input())
    for _ in range(n):
        stack = []
        arr = list(input().rstrip())

        for e in arr:
            if stack and stack[-1] == e:
                stack.pop()
                continue
            stack.append(e)
        
        if not stack: answer += 1
    print(answer)