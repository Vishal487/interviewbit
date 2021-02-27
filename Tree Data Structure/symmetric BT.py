class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def inorder(root, lst):
    if root:
        inorder(root.left, lst)
        lst.append(root.val)
        inorder(root.right, lst)


def isSymmetricUtil(root1, root2):
    if root1 == root2 == None:
        return 1
    if root1 and root2:
        if root1.val == root2.val and isSymmetricUtil(root1.left, root2.right) and isSymmetricUtil(root1.right, root2.left):
            return 1
    return 0

def isSymmetric(root):
    return isSymmetricUtil(root, root)


if __name__ == "__main__":
    mylist = [10, 8, 8, 3, 9, 9, 3]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])
    root.right.right = TreeNode(mylist[6])

    print(isSymmetric(root))


"""
             10
           /   \
          8     8
         / \   / \
        3   9  9  3  
"""