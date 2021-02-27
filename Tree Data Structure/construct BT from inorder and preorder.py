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
    if root is None:
        print("empty")
    inorder(root)
    print("\n")


def buildTree(A, B):
    if A:
        root = TreeNode(A[0])
        idx = B.index(A[0])
        root.left = buildTree(A[1:idx + 1], B[:idx])
        root.right = buildTree(A[idx + 1:], B[idx + 1:])
        return root

    


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    preOrder = [10, 8, 3, 9, 20, 15]
    inOrder = [3, 8, 9, 10, 15, 20]
    new_root = buildTree(preOrder, inOrder)
    printInorder(new_root)

    
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""