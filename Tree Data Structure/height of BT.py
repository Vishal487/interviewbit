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


def height(root):
    if root is None:
        return 0
    curr_ht = 1 + max(height(root.left), height(root.right))
    print("height of node {} is {}".format(root.val, curr_ht))
    return curr_ht

if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    ht = height(root)
    print("height: ", ht)


"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""