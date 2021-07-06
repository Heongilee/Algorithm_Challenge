import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
##################################################################################################
# 29% TLE
#############################################################################################
class Node(object):
    def __init__(self, data=None):
        self.data = data                # 양수형 정수
        self.children = [None, None]    # [왼쪽 자식, 오른쪽 자식]
        self.parent = None              # 부모 노드를 가리킴

class Tree(object):
    def __init__(self, initNode):
        self.root = Node(initNode)
        self.curNode = self.root
        self.pointer = None             # 후위 순회용 포인터

    def insertNumber(self, n):
        while self.curNode.parent != None and n > self.curNode.parent.data:
            self.curNode = self.curNode.parent
        while True:
            if n < self.curNode.data:
                if self.curNode.children[0] == None:
                    self.curNode.children[0] = Node(n)
                    self.curNode.children[0].parent = self.curNode
                    self.curNode = self.curNode.children[0]
                    break
                self.curNode = self.curNode.children[0]
            elif n > self.curNode.data:
                if self.curNode.children[1] == None:
                    self.curNode.children[1] = Node(n)
                    self.curNode.children[1].parent = self.curNode
                    self.curNode = self.curNode.children[1]
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
    for number in sys.stdin: tree.insertNumber(int(number))
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
