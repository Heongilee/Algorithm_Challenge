import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

def isPalindrome(text):
    if(len(text) == 1):
        return True

    lt = 0
    rt = len(text) - 1
    while(lt < rt):
        if(text[lt] != text[rt]):
            return False
        lt += 1
        rt -= 1
    return True

def solution(plain):
    P = list(plain)
    cnt = 0
    while(not isPalindrome(P)):
        P = P[1:]
        cnt += 1
    return len(plain) - cnt

if __name__ == "__main__":
    res = solution(input())
    print(res)