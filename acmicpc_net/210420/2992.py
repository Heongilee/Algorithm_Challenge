import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dic_list = list(map(int, str(n)))
    dic = dict(map(lambda x: (x, dic_list.count(x)), dic_list))
    res = 0

    # cut-edge : 내림차순일경우 답이 없음.
    for i in range(len(dic_list) - 1):
        if dic_list[i] < dic_list[i + 1]:
            break
    else:
        print(res)
        sys.exit(0)

    while True:
        n += 1

        myDict_list = list(map(int, str(n)))
        myDict = dict(map(lambda x: (x, myDict_list.count(x)), myDict_list))
        # cut-edge : 길이가 넘어가면 답이 없음.
        if len(dic_list) != len(myDict_list): break
        else:
            for K, V in dic.items():
                if myDict.get(K, 0) == 0: break
                if myDict[K] != V: break
            else:
                res = n
                break
    print(res)