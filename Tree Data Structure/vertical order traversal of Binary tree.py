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


def findMinMax(root, minimum, maximum, hd):
    if root is None:
        return
    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    
    findMinMax(root.left, minimum, maximum, hd-1)
    findMinMax(root.right, minimum, maximum, hd+1)

def printVerticalLine(root, line_no, hd, row):
    if root is None:
        return
    if hd == line_no:
        row.append(root.val)
        # print(root.val)
    
    printVerticalLine(root.left, line_no, hd-1, row)
    printVerticalLine(root.right, line_no, hd+1, row)

def verticalOrderTraversal(root):
    minimum = [0]
    maximum = [0]
    hd = 0
    findMinMax(root, minimum, maximum, hd)
    ans = []
    for line_no in range(minimum[0], maximum[0]+1):
        row = []
        printVerticalLine(root, line_no, 0, row)  
        ans.append(row)
    return ans


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5]
    root = TreeNode(mylist[0])
    root.left = TreeNode(mylist[1])
    root.right = TreeNode(mylist[2])
    root.left.left = TreeNode(mylist[3])
    root.left.right = TreeNode(mylist[4])
    # root.right.left = TreeNode(mylist[5])

    printInorder(root)
    
    ans = verticalOrderTraversal(root)
    print(ans)



"""
            10
           /  \
          8    20
         / \   /  
        3   9 15    
"""