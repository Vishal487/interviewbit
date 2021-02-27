class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

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


def buildTree(po, io):   # postOrder, inOrder
    if po:
        root = TreeNode(po[-1])
        idx = io.index(po[-1])
        root.left = buildTree(po[:idx], io[:idx])
        root.right = buildTree(po[idx:-1], io[idx + 1:])
        return root

    


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    # printInorder(root)
    postOrder = [ 5, 6, 3, 1, 4, 2, 7 ]
    inOrder = [ 7, 5, 6, 2, 3, 1, 4 ]
    new_root = buildTree(postOrder, inOrder)
    printInorder(new_root)
    postorder(new_root)

    
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""