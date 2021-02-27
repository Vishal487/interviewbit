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


def levelOrder(root):
    queue = []
    if root is None:
        return queue
    queue.append(root)
    ans = []
    while queue:
        popped = queue.pop(0)
        # print(popped.val, end=" ")
        ans.append(popped.val)

        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    return ans

def zigzag_LOT(root):
    def heightOfTree(root):
        if root is None:
            return 0
        else:
            lh = heightOfTree(root.left)
            rh = heightOfTree(root.right)

            return 1+max(lh, rh)

    def printSpecificLevel(root, level, row):
        if root is None:
            return
        if level == 1:
            row.append(root.val)
        printSpecificLevel(root.left, level-1, row)
        printSpecificLevel(root.right, level-1, row)


    height = heightOfTree(root)
    ans = []
    for d in range(1, height+1):
        row = []
        printSpecificLevel(root, d, row)
        if d%2 == 0:
            ans.append(row[::-1])
        else:
            ans.append(row)
    return ans




if __name__ == "__main__":
    mylist = [10, 8, 20, 3, 9, 15]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    print(levelOrder(root))

    print(zigzag_LOT(root))

"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""