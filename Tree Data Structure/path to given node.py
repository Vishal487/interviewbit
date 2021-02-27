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


def findPathUtil(root, node_val, ans):
    if root is None:
        return False
    
    ans.append(root.val)

    if root.val == node_val:
        return True
    
    if findPathUtil(root.left, node_val, ans) or findPathUtil(root.right, node_val, ans):
        return True
    
    ans.pop()
    return False
    


def findPath(root, node_val):   # path always exists
    ans = []
    findPathUtil(root, node_val, ans)
    print(ans)



if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    findPath(root, 10)

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""