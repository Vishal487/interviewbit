class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def printInorder(root):
    inorder(root)
    print("\n")

def diagonalTraversalUtil(root, d, diagonalMap):  # d correspond to a unique diagonal
    if root is None:
        return
    try:
        diagonalMap[d].append(root.val)
    except:
        KeyError
        diagonalMap[d] = [root.val]

    diagonalTraversalUtil(root.left, d+1, diagonalMap)
    diagonalTraversalUtil(root.right, d, diagonalMap)  # d is same for right

def diagonalTraversal(root):
    diagonalMap = dict()
    diagonalTraversalUtil(root, 0, diagonalMap)
    ans = []
    for k,v in diagonalMap.items():
        ans.extend(v)
    return ans



if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print(diagonalTraversal(root))
    
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""