import sys
input = sys.stdin.readline
INF = int(10e4)

class Node(object):
    def __init__(self, emp, weight):
        self.weight = 0    #값
        self.emp = emp  # 판매원 이름
        self.children = {}

class Tree(object):
    def __init__(self):
        self.root = Node("center", 0)
        self.flag = False   # 부모로 올라가는 플래그
        self.tw = 0         # 임시 변수
        self.output = 0

    def DFS(self, curNode, emp_name, ref):
        if curNode.emp == ref:
            curNode.children[emp_name] = Node(emp_name, 0)
        if not curNode.children:
            return
        else:
            for k in curNode.children.keys():
                self.DFS(curNode.children[k], emp_name, ref)

    def insertNode(self, emp_name, ref):
        curNode = self.root
        if ref == '-':
            curNode.children[emp_name] = Node(emp_name, 0)
        else:
            self.DFS(curNode, emp_name, ref)
    
    def DDFS(self, curNode, emp_name, weight):
        if curNode.emp == emp_name:
            self.flag = True
            curNode.weight = weight
            if weight * 0.1 > 0:
                self.tw = weight * 0.1
            return
        if not curNode.children:
            return
        else:
            for k in curNode.children.keys():
                self.DDFS(curNode.children[k], emp_name, weight)
                if self.flag:
                    curNode.weight += self.tw
                    if self.tw * 0.1 > 0:
                        self.tw *= 0.1
                        return

    def calculateWeight(self, emp_name, weight):
        curNode = self.root
        self.DDFS(curNode, emp_name, weight)
    
    def DDDFS(self, curNode, emp_name):
        if not curNode.children:
            return
        if curNode.emp == emp_name:
            self.output = curNode.weight
            self.flag = True
            return
        else:
            for k in curNode.children.keys():
                self.DDDFS(curNode.children[k], emp_name)
                if self.flag:
                    return
    
    def findCost(self, emp_name):
        self.flag = False
        curNode = self.root
        self.DDDFS(curNode, emp_name)

        return int(self.output)


# enroll : 판매원의 이름
# referral : 다단계 조직에 참여시킨 다른 판매원의 이름
# seller : 판매량 집계 데이터의 판매원 이름
# amount : 판매량 집계 데이터의 판매 수량
def solution(enroll, referral, seller, amount):
    T = Tree()
    res = []
    for i in range(len(enroll)):
        T.insertNode(enroll[i], referral[i])
    
    for i in range(len(seller)):
        T.calculateWeight(seller[i], amount[i] * 100)
    
    for i in range(len(enroll)):
        r = T.findCost(enroll[i])
        res.append(r)

    return res

if __name__ == '__main__':
    res = solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], 
                     ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], 
                    ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
    print(res)
    # answer : [360, 958, 108, 0, 450, 18, 180, 1080]
    # output : ?