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


def sortedArrayToBST(A):
    if len(A) == 0:
        return
    mid_ind = len(A)//2
    mid_val = A[mid_ind]
    nn = TreeNode(mid_val)
    nn.left = sortedArrayToBST(A[:mid_ind])
    nn.right = sortedArrayToBST(A[mid_ind+1:])    
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
    
    new_root = sortedArrayToBST([1,2,3,4,5,6])
    printInorder(new_root)
    print(new_root.val)
    print(new_root.left.val)
    print(new_root.right.val)

    
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""