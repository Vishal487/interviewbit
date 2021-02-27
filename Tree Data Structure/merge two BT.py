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

def mergeTwoBTUtil(root1, root2):
    if root1 and root2:
        root1.val = root1.val + root2.val
        root1.left = mergeTwoBTUtil(root1.left, root2.left)
        root1.right = mergeTwoBTUtil(root1.right, root2.right)
    elif root2:
        return root2
    else:
        return root1
    return root1

def mergeTwoBT(root1, root2):
    temp1 = root1
    temp2 = root2
    mergeTwoBTUtil(temp1, temp2)
    return root1




if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    # root.left.left = TreeNode(mylist[3])
    # root.left.right = TreeNode(mylist[4])
    # root.right.left = TreeNode(mylist[5])

    mylist = [10, 8, 20, 3, 9, 15]
    root2 = TreeNode(mylist[0])
    root2.left = TreeNode(mylist[1])
    root2.right = TreeNode(mylist[2])
    root2.left.left = TreeNode(mylist[3])
    root2.left.right = TreeNode(mylist[4])
    root2.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    printInorder(root2)

    nr = mergeTwoBT(root, root2)

    printInorder(nr)

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""