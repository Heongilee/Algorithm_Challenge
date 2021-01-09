import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

def solution(arr):
    Count = [0] * (max(arr) + 1)
    Res = []

    for e in arr:
        Count[e] += 1
    
    for i in range(len(Count)): # Count배열을 순회하며
        for j in range(Count[i]):   # Count개수만큼 반복시켜 인덱스 i를 찍어준다.
            Res.append(i)
    return Res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solution(arr)
    print(res)