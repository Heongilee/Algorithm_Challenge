from collections import deque
def solution(n, recipes, orders):
    orders = deque(orders)
    F = [1] * n
    R = len(recipes)
    t = 1
    cuisine = []
    res = -1
    for r in recipes:
        rm, rt = r.split(" ")
        rt = int(rt)
        cuisine.append((rm, rt))
    
    while(orders):
        om, ot = orders.popleft().split(" ")
        ot = int(ot)
        if(t >= ot):
            for i in range(n):
                if(F[i] <= t):
                    for j in range(R):
                        if(cuisine[j][0] == om):
                            F[i] = t + cuisine[j][1]
                            if(not orders):
                                res = F[i]
                            break
                    break
                else:
                    continue
            else:
                orders.appendleft(om + " " + str(ot))
                t += 1
        else:
            orders.appendleft(om + " " + str(ot))
            t += 1
    return res

if __name__ == '__main__':
    res = solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"])
    print(res)