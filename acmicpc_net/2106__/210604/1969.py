import sys, string
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    n, m = map(int, input().split())
    dna_list = []
    for i in range(n):
        dna_list.append(sys.stdin.readline().replace('\n', ''))

    cnt_dict = dict()
    hd = 0
    result = ''
    for i in range(m):
        cnt_dict.update(zip([alpha for alpha in string.ascii_uppercase], [0 for _ in range(26)]))
        for j in range(n):
            cnt_dict[dna_list[j][i]] += 1
        max = 0
        alpha =''
        for k in string.ascii_uppercase:
            if max < cnt_dict[k]:
                max = cnt_dict[k]
                alpha = k
            hd += cnt_dict[k]
        result += alpha
        hd -= cnt_dict[alpha]
    print(result)
    print(hd)
'''
from collections import defaultdict
input = sys.stdin.readline

INF = int(10e9)
if __name__ == '__main__':
    # N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수
    n, m = map(int, input().split())
    dnas = [input().rstrip() for _ in range(n)]
    hammingDist = 0
    S = ""
    
    for i in range(m):
        myList = []
        tmp = [dnas[j][i] for j in range(n)]
        dic = defaultdict(int)
        for e in tmp: dic[e] += 1
        for k, v in dic.items(): myList.append((k, v))
        
        myList.sort(key=lambda X: (-X[1], X[0]))
        hammingDist += sum(map(lambda j : 1 if myList[0][0] != tmp[j] else 0, range(n)))
        S += myList[0][0]
    print(S)
    print(hammingDist)

'''