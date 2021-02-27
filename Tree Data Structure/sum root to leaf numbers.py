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

def sumNumbersUtil(root, ansList, ssf):
    if root is None:
        return
    ssf += str(root.val)
    if root.left == root.right == None:
        ansList.append(ssf)
    sumNumbersUtil(root.left, ansList, ssf)
    sumNumbersUtil(root.right, ansList, ssf)

def sumNumbers(root):
    ansList = []
    sumNumbersUtil(root, ansList, "")
    print(ansList)
    ans = 0
    for numStr in ansList:
        ans += int(numStr)
    return ans


if __name__ == "__main__":
    mylist = [6, 3, 5, 2, 5, 7, 4, 4]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])

    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])

    root.left.right.left = TreeNode(mylist[5])
    root.left.right.right = TreeNode(mylist[6])

    root.right.right = TreeNode(mylist[7])

    printInorder(root)
    
    print(sumNumbers(root))
"""
            0
           /  \
          8    2
         / \   /  
        3   9 1    
"""