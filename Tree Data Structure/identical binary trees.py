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


def isIdenticalBTsUtil(root1, root2, flag):
    # print(flag)
    if root1 and root2:
        if root1.val != root2.val:
            flag[0] = 1
            return
    elif root1 and root2 is None:
        flag[0] = 1
        return
    elif root2 and root1 is None:
        flag[0] = 1
        return
    else:
        return
    isIdenticalBTsUtil(root1.left, root2.left, flag)
    isIdenticalBTsUtil(root1.right, root2.right, flag)

def isIdenticalBTs(root1, root2):
    flag = [0]
    isIdenticalBTsUtil(root1, root2, flag)
    return int(not flag[0])


# simple and intuitive
def isIdenticalBTs_simple(root1, root2):
    if root1 == root2 == None:
        return True
    if root1 and root2:
        if root1.val == root2.val and isIdenticalBTs_simple(root1.left, root2.left) and isIdenticalBTs_simple(root1.right, root2.right):
            return True
    return False


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    mylist = [10, 8, 20, 3, 9, 15]
    root2 = TreeNode(mylist[0])
    root2.left = TreeNode(mylist[1])
    root2.right = TreeNode(mylist[2])
    root2.left.left = TreeNode(mylist[3])
    root2.left.right = TreeNode(mylist[4])
    # root2.right.left = TreeNode(mylist[5])


    printInorder(root)
    printInorder(root2)

    print(isIdenticalBTs(root, root2))
    print(isIdenticalBTs_simple(root, root2))


"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""