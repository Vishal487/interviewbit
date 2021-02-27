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


def buildTree(A):
    if len(A) == 0:
        return
    max_val = max(A)
    max_ind = A.index(max_val)

    nn = TreeNode(max_val)
    nn.left = buildTree(A[:max_ind])
    nn.right = buildTree(A[max_ind+1:])
    return nn


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    new_root = buildTree([1,2,3])
    printInorder(new_root)
    
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""