import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

'''
# ' '이나 '-'으로 단어 구분
# 앞 단어가 ce, je, ne, me, te, se, le, la, de, que || si 이고
# 뒷 단어가 모음 a, e, i, o, u, h으로 시작하는 경우
# 앞 단어의 마지막 모음(vowel)이 사라지는 대신 어퍼스트로피' 가 붙으면서 이어짐.
'''
if __name__ == '__main__':
    arr = []
    myString = input().rstrip().split("-")
    dic = dict(zip(['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu'], ['e'] * 9))
    vowels = ['a', 'e', 'i', 'o', 'u', 'h']
    for s in myString:
        arr += list(s.split(" "))
    i = 0
    while i < len(arr):
        t = arr[i].find("\'")
        if t == -1: 
            i += 1
            continue
        
        subLt = arr[i][:t]
        subRt = arr[i][t + 1:len(arr[i])]
        if subRt[0] not in vowels:
            i += 1
            continue
        k = dic.get(subLt, None)
        if k == None:
            i += 1
            continue
        arr.pop(i)
        arr.insert(i, subRt)
        arr.insert(i, subLt + k)
        i += 2
    # print(arr)
    print(len(arr))
    