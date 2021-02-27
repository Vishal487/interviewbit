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

def isValidBSTUtil(root, MIN, MAX):
    if root is None:
        return True
    if MIN < root.val < MAX and isValidBSTUtil(root.left, MIN, root.val) and isValidBSTUtil(root.right, root.val, MAX):
        return True
    return False

def isValidBST(root):
    return isValidBSTUtil(root, -999999, 9999999)
    
    


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print(isValidBST(root))

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""