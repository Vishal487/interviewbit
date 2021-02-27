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

def hasPathSum(root, target):
    def hasPathSumUtil(root, curr_sum):
        if root is None:
            return 0
        if root.val+curr_sum == target and not root.left and not root.right:
            return 1
        return (hasPathSumUtil(root.left, curr_sum+root.val)) or (hasPathSumUtil(root.right, curr_sum+root.val))
    
    return hasPathSumUtil(root, 0)





if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print(hasPathSum(root, 27))
"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""