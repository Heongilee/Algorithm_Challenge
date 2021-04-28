import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key      # char 문자
        self.data = data    # 기존 방식에선 T/F를 집어넣지만, 여기선 string or None을 집어넣음.
        self.children = {}  # 해당 char에서 다른 char로 이어지는 children character(key)들과 각 Node(value)

class Trie(object):
    def __init__(self):
        self.head = Node(key=None, data=None)   # root 노드 생성.
    
    def insert_string(self, input_string):
        cur_node = self.head

        for c in input_string:
            if c not in cur_node.children.keys():
                cur_node.children[c] = Node(key=c)
            cur_node = cur_node.children[c]
        cur_node.data = input_string # leaf노드에는 부모를 거쳐오면서 만들어진 단어를 data에 바인딩함.
    
    def search_string(self, input_string):
        cur_node = self.head

        for c in input_string:
            if c not in cur_node.children.keys():
                return False
            else:
                cur_node = cur_node.children[c] # step into next character
        
        if cur_node.data == input_string:
            return True
        else:
            return False
    
    def start_with(self, prefix):
        cur_node = self.head
        words = []  # prefix로 시작하는 모든 워드를 찾아 리턴할 리스트.
        subtrie = None
        for c in prefix:
            if c in cur_node.children.keys():
                cur_node = cur_node.children[c]
                subtrie = cur_node
            else:
                return []
        
        # 이제 prefix가 존재한다는 것을 알았고, subtrie에 있는 모든 워드를 찾아서 리턴하면 됨.
        cur_nodes = [subtrie]
        next_nodes = []
        while True:
            for c in cur_nodes:
                if c.data != None:
                    words += [c.data]
                next_nodes += list(c.children.values())
            
            if len(next_nodes) == 0:
                break
            else:
                cur_nodes = next_nodes
                next_nodes = []

        return words
            

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        trie = Trie()
        words = [input().rstrip() for _ in range(n)]

        for i in range(n):
            trie.insert_string(words[i])
        
        for i in range(n):
            tmp = set(trie.start_with(words[i])).difference([words[i]])

            if tmp:
                print("NO")
                break
            else:
                continue
        else:
            print("YES")