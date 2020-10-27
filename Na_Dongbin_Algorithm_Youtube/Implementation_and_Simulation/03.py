import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == "__main__":
    command = [[[(0, -2), (-1, 0)], [(0, -2), (1, 0)], [(0, 2), (-1, 0)], [(0, 2), (1, 0)]], 
           [[(-2, 0), (0, -1)], [(-2, 0), (0, 1)], [(2, 0), (0, -1)], [(2, 0), (0, 1)]]]
    col = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [0, 1, 2, 3, 4, 5, 6, 7]))
    
    N = list(input())
    p = (int(col.get(N[0])), int(N[1]) - 1)
    count = 0
    
    for com in command:
        for c in com:
            for i in range(2):
                xx = p[0] + c[i][0]
                yy = p[1] + c[i][1]
                if((xx < 0 or xx >= 8) or (yy < 0 or yy >= 8)):
                    break
            else:
                count += 1

    print(count)
    