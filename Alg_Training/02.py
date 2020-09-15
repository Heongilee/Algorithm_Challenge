import sys
import heapq as hq
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def Preorder_Traversal(a, i):
    if(i + 1 > len(a)):
        return
    else:
        print(a[i], end=' ')
        Preorder_Traversal(a, i * 2)
        Preorder_Traversal(a, i * 2 + 1)
        
def Inorder_Traversal(a, i):
    if(i + 1 > len(a)):
        return
    else:
        Inorder_Traversal(a, i * 2)
        print(a[i], end=' ')
        Inorder_Traversal(a, i * 2 + 1)

# 후위순회의 대표적인 예 : Merge-sort
def Postorder_Traversal(a, i):
    if(i + 1 > len(a)):
        return
    else:
        Postorder_Traversal(a, i * 2)
        Postorder_Traversal(a, i * 2 + 1)
        print(a[i], end=' ')

if __name__ == "__main__":
    a = []
    for i in range(8):
        hq.heappush(a, i)
        
    Preorder_Traversal(a, 1)
    print()
    Inorder_Traversal(a, 1)
    print()
    Postorder_Traversal(a, 1)
    