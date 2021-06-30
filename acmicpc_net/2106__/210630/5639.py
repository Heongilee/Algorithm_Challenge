import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
##################################################################################################
# 27% TLE
#############################################################################################
class Node(object):
    def __init__(self, data = None):
        self.data = data # 양수형 정수
        self.children = [None, None]
        # self.parent = None

class Tree(object):
    def __init__(self, initNode):
        self.root = Node(initNode)
        self.curNode = self.root
        self.pointer = None
    
    # ! 1만번의 입력마다 O(logN)을 수행하면 시간이 낭비될 수 있음.
    def insertNumber(self, n):
        self.curNode = self.root
        while True:
            if n < self.curNode.data:
                if self.curNode.children[0] == None:
                    self.curNode.children[0] = Node(n)
                    break
                self.curNode = self.curNode.children[0]
            elif n > self.curNode.data:
                if self.curNode.children[1] == None:
                    self.curNode.children[1] = Node(n)
                    break
                self.curNode = self.curNode.children[1]


    def preorderTraversal(self, ptr):
        pNode = self.pointer
        self.pointer = ptr
        if self.pointer == None:
            self.pointer = pNode
            return
        
        self.preorderTraversal(self.pointer.children[0])
        self.preorderTraversal(self.pointer.children[1])
        print(self.pointer.data)
        self.pointer = pNode
            
if __name__ == '__main__':
    tree = Tree(int(input()))
    for number in sys.stdin: 
        tree.insertNumber(int(number))
    tree.preorderTraversal(tree.root)
    

##################################################################################################
# RE(Index Error) :: 노드가 10000개 까지 올 수 있기 때문에, 배열크기는 2^10000이 필요하게 된다.
#############################################################################################
'''
def parent(ptr):
    return ptr // 2

def leftChild(ptr):
    return ptr * 2

def rightChild(ptr):
    return ptr * 2 + 1

def pot(p):
    if tree[p] == None:
        return
    
    pot(p * 2)
    pot(p * 2 + 1)
    print(tree[p])

INF = int(10e6) + 1
if __name__ == '__main__':
    tree = [None] * INF
    ptr = 1

    # insert Node
    firstInput = False
    for number in sys.stdin:
        n = int(number)

        if not firstInput:    # root-node
            firstInput = True
            tree[ptr] = n
        elif n < tree[ptr]:
            ptr = leftChild(ptr)
            tree[ptr] = n
        elif n > tree[ptr]:
            while parent(ptr) > 0 and n > tree[parent(ptr)]:
                ptr = parent(ptr)
            ptr = rightChild(ptr)
            tree[ptr] = n
    
    # Post-order traversal
    pot(1)
'''