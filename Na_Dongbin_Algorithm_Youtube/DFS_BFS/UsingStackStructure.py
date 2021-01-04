import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    stack = []
    stack.append(5)
    stack.append(3)
    stack.append(2)
    stack.append(7)

    print(stack)

    stack.pop()
    print(stack[::-1])  # Stack의 최상단 원소부터 출력
    print(stack)        # Stack의 최하단 원소부터 출력

