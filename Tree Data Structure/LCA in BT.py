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

def findPath(root, value, path):
    if root is None:
        return False

    path.append(root.val)

    if root.val == value:
        return True

    if (root.left and findPath(root.left, value, path) ) or (root.right and findPath(root.right, value, path)):
        return True

    path.pop()
    return False
    

def LCA(root, val1, val2):
    path1 = []
    path2 = []

    if (not findPath(root, val1, path1) ) or (not findPath(root, val2, path2)):
        return -1
    
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print("lca : ", LCA(root, 3, 8))
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""