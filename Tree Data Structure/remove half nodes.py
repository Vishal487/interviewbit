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


def removeHalf(root):
    if root is None:
        return None
    
    root.left = removeHalf(root.left)
    root.right = removeHalf(root.right)

    if root.left is None and root.right is None:
        return root
    
    if root.left is None:    # right is there
        new_root = root.right
        temp = root
        root = None
        del(temp)
        return new_root

    if root.right is None:
        new_root = root.left
        temp = root
        root = None
        del(temp)
        return new_root
    
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

    new_root = removeHalf(root)

    printInorder(new_root)
    

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""
